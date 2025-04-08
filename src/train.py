### FILE: src/train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(df):
    X = df.drop(columns=['Credit_Score'])
    y = df['Credit_Score']

    from sklearn.preprocessing import LabelEncoder
    y = LabelEncoder().fit_transform(y)

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, 'models/X_train_cols.pkl')
    return model, X_val, y_val