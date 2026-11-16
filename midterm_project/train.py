
import pickle
from pathlib import Path
from urllib.request import urlretrieve

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error


# file paths
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / 'data' / 'listings.csv'
MODEL_FILE = BASE_DIR / 'model.bin'

DATA_URL = (
    'https://data.insideairbnb.com/germany/be/berlin/'
    '2026-06-26/visualisations/listings.csv'
)

# download dataset if necessary
if not DATA_FILE.exists():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    print('Downloading Berlin Airbnb dataset...')
    urlretrieve(DATA_URL, DATA_FILE)


# load and clean data
df = pd.read_csv(DATA_FILE)
df = df.dropna(subset=['price']).copy()
df = df[(df['price'] > 0) & (df['price'] <= 650)].copy()

features = [
    'neighbourhood_group',
    'room_type',
    'latitude',
    'longitude',
    'minimum_nights',
    'number_of_reviews',
    'reviews_per_month',
    'availability_365'
]

df = df[features + ['price']].fillna(0)

# standardize categorical values
categorical = ['neighbourhood_group', 'room_type']

for col in categorical:
    df[col] = df[col].str.lower().str.replace(' ', '_')


# split data (80% training, 20% test)
df_full_train, df_test = train_test_split(
    df, test_size=0.2, random_state=1
)

y_full_train = np.log1p(df_full_train['price'].values)
y_test = np.log1p(df_test['price'].values)

df_full_train = df_full_train.drop(columns=['price'])
df_test = df_test.drop(columns=['price'])


# encode features
dv = DictVectorizer(sparse=False)

X_full_train = dv.fit_transform(
    df_full_train.to_dict(orient='records')
)

X_test = dv.transform(
    df_test.to_dict(orient='records')
)


# train final model
model = RandomForestRegressor(
    n_estimators=100,
    max_depth=15,
    min_samples_leaf=1,
    random_state=1,
    n_jobs=-1
)

model.fit(X_full_train, y_full_train)


# evaluate on test data
y_pred = model.predict(X_test)

rmse_log = np.sqrt(mean_squared_error(y_test, y_pred))
rmse_eur = np.sqrt(
    mean_squared_error(np.expm1(y_test), np.expm1(y_pred))
)
mae_eur = mean_absolute_error(
    np.expm1(y_test), np.expm1(y_pred)
)

print(f'Test RMSE (log): {rmse_log:.4f}')
print(f'Test RMSE (EUR): {rmse_eur:.2f}')
print(f'Test MAE (EUR): {mae_eur:.2f}')


# export model and vectorizer
with open(MODEL_FILE, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f'Model saved to {MODEL_FILE}')