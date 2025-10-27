import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import os

# Define the input data structure
class Client(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

# Load the pipeline from the path inside the Docker container
PIPELINE_PATH = "/code/pipeline_v2.bin"

with open(PIPELINE_PATH, 'rb') as f_in:
    pipeline = pickle.load(f_in)

app = FastAPI()

@app.post("/predict")
def predict(client: Client):
    client_dict = client.model_dump()
    probability = pipeline.predict_proba([client_dict])[0, 1]
    return {"conversion_probability": probability, "model_version": "v2"}