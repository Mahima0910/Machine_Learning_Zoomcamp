FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY train.ipynb .
COPY predict.py .
COPY data.csv . 
# Note: In a real scenario, you might pull data from a bucket or mount it, 


# Train the model during build (optional, or copy a pre-trained model.joblib)
# RUN python train.ipynb

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "predict:app"]