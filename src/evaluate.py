### FILE: src/evaluate.py
from sklearn.metrics import accuracy_score, classification_report

def evaluate_model(model, X_val, y_val):
    y_pred = model.predict(X_val)
    print("Accuracy:", accuracy_score(y_val, y_pred))
    print("Classification Report:\n", classification_report(y_val, y_pred))