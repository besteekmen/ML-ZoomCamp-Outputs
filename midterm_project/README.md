
# Berlin Airbnb Price Prediction

## 1. Problem Description

This project predicts the nightly rental price of Airbnb listings in Berlin, Germany, using machine learning.

Airbnb prices depend on several characteristics, including location, accommodation type, minimum stay requirements, availability, and guest reviews.

The goal is to build a regression model that estimates listing prices based on these characteristics and deploy it as a prediction service using FastAPI and Docker.

This project was developed for the DataTalksClub Machine Learning Zoomcamp 2026 midterm project.

## 2. Dataset

**Source:** [Inside Airbnb](https://insideairbnb.com/get-the-data/)

**Dataset:** Berlin, Germany — Summary Listings, June 26, 2026

**CSV:** [Download listings.csv](https://data.insideairbnb.com/germany/be/berlin/2026-06-26/visualisations/listings.csv)

The original dataset contains 12,855 listings and 19 columns.

### Data Preparation

The following preprocessing steps were applied:

1. Remove listings with missing or nonpositive prices.
2. Exclude extreme prices above €650, approximately the 99th percentile.
3. Select eight relevant input features.
4. Fill missing feature values with zero.
5. Standardize categorical values to lowercase and replace spaces with underscores.
6. Apply `log1p()` to the target variable.
7. Encode categorical features using `DictVectorizer`.

### Selected Features

| Feature | Description |
|---|---|
| `neighbourhood_group` | Berlin district |
| `room_type` | Type of accommodation |
| `latitude` | Geographic latitude |
| `longitude` | Geographic longitude |
| `minimum_nights` | Minimum required stay |
| `number_of_reviews` | Total number of reviews |
| `reviews_per_month` | Average monthly reviews |
| `availability_365` | Available days in the next 365 days |

**Target:** `price` (EUR)

## 3. Exploratory Data Analysis

The notebook investigates:

- Missing values and dataset structure
- Price distribution and extreme values
- Differences in prices across room types
- Log transformation of the target
- Feature importance from the selected Random Forest model

### Main Findings

The original price distribution is strongly right-skewed, with some very expensive listings.

Entire homes and apartments generally have higher prices than private and shared rooms.

The Random Forest feature importance analysis identifies `minimum_nights` as the most influential predictor (approximately 70.9% impurity-based importance), followed by accommodation type and geographic coordinates.

This importance does not establish a causal relationship.

Detailed analysis and visualizations are available in `notebook.ipynb`.

## 4. Model Training and Evaluation

Three regression algorithms were evaluated:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor

The tree-based models were tuned using different hyperparameters.

The development data was split into training and validation sets for model comparison. The test set was reserved for final evaluation.

### Validation Results

| Model | Configuration | RMSE (log) | RMSE (EUR) |
|---|---|---:|---:|
| Linear Regression | Default | 0.4680 | 85.23 |
| Decision Tree | max_depth=5 | 0.4541 | 86.70 |
| Decision Tree | max_depth=10 | 0.4591 | 85.37 |
| Random Forest | max_depth=10, min_samples_leaf=1 | 0.4209 | 80.89 |
| Random Forest | max_depth=15, min_samples_leaf=1 | 0.4178 | **78.88** |
| Random Forest | max_depth=15, min_samples_leaf=5 | **0.4151** | 79.14 |

RMSE in euros was selected as the primary metric.

### Selected Model

**Random Forest Regressor**

- `n_estimators=100`
- `max_depth=15`
- `min_samples_leaf=1`
- `random_state=1`

The selected model was retrained using the combined training and validation data.

### Final Test Results

| Metric | Result |
|---|---:|
| RMSE (log) | 0.4083 |
| RMSE (EUR) | €76.17 |
| MAE (EUR) | €48.30 |

The final model achieves an average absolute error of approximately €48.30 on the held-out test set.

These results apply to the filtered dataset and do not guarantee equivalent performance on future listings.

## 5. Project Structure

```text
midterm_project/
├── notebook.ipynb       # EDA, model training, and evaluation
├── train.py             # Reproducible training script
├── predict.py           # FastAPI prediction service
├── model.bin            # Exported model and DictVectorizer
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
├── README.md            # Project documentation
└── data/
    └── listings.csv     # Downloaded dataset
```

The training script automatically downloads the dataset if `data/listings.csv` is missing.

## 6. Environment Setup

Python 3.12 is recommended.

Clone the repository:

```bash
git clone https://github.com/besteekmen/ML-ZoomCamp-Outputs.git
cd ML-ZoomCamp-Outputs/midterm_project
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Alternatively, using `uv`:

```bash
uv venv --python 3.12
source .venv/bin/activate
uv pip install -r requirements.txt
```

To run the notebook, additionally install:

```bash
uv pip install jupyter matplotlib seaborn
```

## 7. Reproduce Model Training

From the `midterm_project` directory:

```bash
python train.py
```

The script:

1. Downloads the dataset if necessary.
2. Cleans and preprocesses the data.
3. Splits the data into development and test sets.
4. Trains the selected Random Forest model.
5. Evaluates performance on the test set.
6. Exports the trained model and vectorizer to `model.bin`.

Expected test results:

```text
Test RMSE (log): 0.4083
Test RMSE (EUR): 76.17
Test MAE (EUR): 48.30
```

## 8. Run the Prediction API Locally

Start the FastAPI application:

```bash
uvicorn predict:app --host 0.0.0.0 --port 9696
```

Check the health endpoint:

```bash
curl http://localhost:9696/health
```

Expected response:

```json
{"status":"ok"}
```

### Make a Prediction

```bash
curl -X POST http://localhost:9696/predict \
  -H "Content-Type: application/json" \
  -d '{
    "neighbourhood_group": "Mitte",
    "room_type": "Entire home/apt",
    "latitude": 52.5200,
    "longitude": 13.4050,
    "minimum_nights": 2,
    "number_of_reviews": 25,
    "reviews_per_month": 1.5,
    "availability_365": 180
  }'
```

Example response:

```json
{"predicted_price_eur":261.99}
```

Interactive API documentation is available at:

http://localhost:9696/docs

## 9. Docker Deployment

Build the Docker image from the `midterm_project` directory:

```bash
docker build -t berlin-airbnb-price .
```

Run the container:

```bash
docker run --rm -p 9696:9696 berlin-airbnb-price
```

The API is available at:

http://localhost:9696

Test it using the same `/health` and `/predict` requests shown above.

The Docker container includes the trained model and all dependencies needed for inference.

Both endpoints were successfully tested inside Docker.

## 10. Limitations and Future Improvements

- The model was trained on a single Berlin dataset snapshot.
- Listings with missing prices and extreme prices above €650 were excluded.
- Missing numerical values were filled with zero, which may not always represent their true meaning.
- `minimum_nights` has unusually high feature importance and deserves further investigation.
- Additional features and more extensive hyperparameter tuning could improve accuracy.
- The API currently runs locally or in Docker; it has not been deployed to a public cloud service.

## 11. Acknowledgements

- [DataTalksClub Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp)
- [Inside Airbnb](https://insideairbnb.com/)
- Berlin Airbnb listings dataset, June 26, 2026