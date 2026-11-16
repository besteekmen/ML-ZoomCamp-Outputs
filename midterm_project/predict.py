import pickle
from pathlib import Path

import numpy as np
from fastapi import FastAPI


# load the trained model and vectorizer
MODEL_FILE = Path(__file__).resolve().parent / 'model.bin'

with open(MODEL_FILE, 'rb') as f_in:
    dv, model = pickle.load(f_in)

# create FastAPI application
app = FastAPI(title='Berlin Airbnb Price Prediction')

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.post('/predict')
def predict(listing: dict):
    # standardize categorical values as in training
    listing = listing.copy()

    for col in ['neighbourhood_group', 'room_type']:
        if col in listing and isinstance(listing[col], str):
            listing[col] = listing[col].lower().replace(' ', '_')

    # transform input features
    X = dv.transform([listing])

    # predict log-price and convert back to euros
    log_price = model.predict(X)[0]
    price = np.expm1(log_price)

    return {
        'predicted_price_eur': round(float(price), 2)
    }