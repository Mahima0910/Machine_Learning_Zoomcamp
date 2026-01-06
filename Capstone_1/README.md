# Student Dropout Prediction

## Problem Description
This project aims to predict whether a student will dropout, enroll, or graduate based on their demographics, socio-economic factors, and academic performance. The goal is to help educational institutions identify students at risk of dropping out.

## Dataset
The dataset `data.csv` contains information on marital status, application mode, grades, and economic indicators.
- **Target Variable**: `Target` (Dropout, Enrolled, Graduate)

## Project Structure
- `notebook.ipynb`: Exploratory Data Analysis and model experimentation.
- `train.py`: Script to train the Random Forest model and save it as `model.joblib`.
- `predict.py`: Flask application to serve the model as an API.
- `Dockerfile`: Configuration to containerize the application.

## How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt