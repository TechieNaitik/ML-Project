### FILE: src/explain.py
import shap
import matplotlib.pyplot as plt


def explain_model(model, X_val, sample_size=100):
    sample = X_val.sample(min(sample_size, len(X_val)), random_state=42)

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(sample)

    print("\\nSHAP Summary Plot (Feature Importance):")
    shap.summary_plot(shap_values, sample, plot_type="bar")

def get_shap_plot(model, X_val, sample_size=100):
    import shap
    import matplotlib.pyplot as plt
    import io
    import base64

    sample = X_val.sample(min(sample_size, len(X_val)), random_state=42)
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(sample)

    fig = shap.summary_plot(shap_values, sample, plot_type="bar", show=False)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf