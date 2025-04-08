### FILE: main.py
import pandas as pd
from src.preprocessing import preprocess_data
from src.train import train_model
from src.evaluate import evaluate_model
from src.explain import explain_model

# Load data
train_df = pd.read_csv("data/train.csv", low_memory=False)

# Preprocess
train_cleaned, _ = preprocess_data(train_df)

# Train
model, X_val, y_val = train_model(train_cleaned)

# Evaluate
evaluate_model(model, X_val, y_val)

# Explain
explain_model(model, X_val, sample_size=100)