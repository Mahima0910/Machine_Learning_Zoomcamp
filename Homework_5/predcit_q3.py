import pickle
# Load the pipeline
with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

# Data for the record to score
client = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

# Predict the probability
# The model expects a list of dictionaries
probability = pipeline.predict_proba([client])[0, 1]

print(f"The probability that this lead will convert is: {probability:.3f}")