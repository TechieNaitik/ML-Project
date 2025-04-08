# Credit Score Predictor with Explainable AI

This project predicts a person's credit score using a machine learning model and explains the results using SHAP (SHapley Additive exPlanations).

## 🔍 Features
- Data cleaning and preprocessing
- Random Forest model training
- Model evaluation
- SHAP-based explainability for predictions

## 📁 Project Structure
```
ML-Project/
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── sample_test.csv
|── models/
|   |── credit_model.pkl
├── notebooks/
│   ├── evaluate.ipynb
│   ├── explain.py
│   ├── main.ipynb
│   └── preprocessing.ipynb
|   ├── test.ipynb
│   └── train.ipynb
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   ├── evaluate.py
│   └── explain.py
├── main.py
├── README.md
|── requirements.txt
|── run.py
├── test.py
```

## 🚀 How to Run
1. Clone the repo
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Train the model:
```bash
python main.py
```

---
Made with ⚡ by an AIML B.Tech student for submission glory
