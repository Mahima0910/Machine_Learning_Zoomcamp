import joblib
import pandas as pd
from flask import Flask, request, jsonify

app = Flask('dropout_prediction')

# Load the model
model = joblib.load(r'C:\Users\HP\OneDrive\Desktop\New folder\model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    customer_data = request.get_json()
    
    # Convert JSON to DataFrame (ensure columns match training)
    df_input = pd.DataFrame([customer_data])
    
    # Predict
    prediction = model.predict(df_input)
    result = prediction[0]
    
    return jsonify({'prediction': result})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)