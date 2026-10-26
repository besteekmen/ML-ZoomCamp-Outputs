import pickle

# load the pretrained model
with open("pipeline.bin", "rb") as f_in:
    model = pickle.load(f_in)

# inspect the loaded object
# print(type(model))

# lead information
lead = {
  "lead_source": "paid_ads",
  "industry": "technology",
  "employment_status": "employed",
  "location": "north_america",
  "number_of_courses_viewed": 2,
  "annual_income": 79276.0,
  "interaction_count": 4,
  "lead_score": 0.41
}

# predict the probability
prob = model.predict_proba([lead])[0, 1]

print(f"Conversion probability: {prob:.3f}")