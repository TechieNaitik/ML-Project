### FILE: src/preprocessing.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df, is_train=True):
    drop_cols = ['ID', 'Customer_ID', 'SSN', 'Name', 'Month']
    df.drop(columns=drop_cols, inplace=True, errors='ignore')

    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    df = df[df['Age'].between(18, 100)]

    df.loc[:, :] = df.replace("_______", np.nan)
    df = df.dropna()

    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str)

    label_encoders = {}
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str)
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    return df, label_encoders