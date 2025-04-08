### FILE: test.py
import pandas as pd
import joblib
from src.preprocessing import preprocess_data

# Load test data
test_df = pd.read_csv("data/test.csv", low_memory=False)

# Preprocess test data
test_cleaned, _ = preprocess_data(test_df, is_train=False)

# Load trained model
model = joblib.load("models/credit_model.pkl")

# Predict
predictions = model.predict(test_cleaned)
print("\nPredicted Credit Scores for test.csv:")
print(predictions)
