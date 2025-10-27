import pickle
from fastapi import FastAPI
from pydantic import BaseModel

# Define the input data structure
class Client(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

# Load the pipeline
with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

app = FastAPI()

@app.post("/predict")
def predict(client: Client):
    # Convert Pydantic model to dict
    client_dict = client.model_dump()

    # Make prediction
    probability = pipeline.predict_proba([client_dict])[0, 1]

    return {"conversion_probability": probability}