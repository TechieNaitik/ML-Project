import pandas as pd

# Create dummy data based on the assumed structure
data = {
    "Age": [30, 45],
    "Occupation": ["Engineer", "Doctor"],
    "Annual_Income": [800000, 1200000],
    "Monthly_Inhand_Salary": [65000, 100000],
    "Num_Bank_Accounts": [3, 5],
    "Num_Credit_Card": [2, 4],
    "Interest_Rate": [10, 12],
    "Num_of_Loan": [1, 3],
    "Delay_from_due_date": [5, 2],
    "Num_of_Delayed_Payment": [2, 1],
    "Changed_Credit_Limit": [5000, 10000],
    "Num_Credit_Inquiries": [1, 2],
    "Credit_Mix": ["Good", "Standard"],
    "Outstanding_Debt": [200000, 300000],
    "Credit_Utilization_Ratio": [0.3, 0.5],
    "Credit_History_Age": ["5 Years and 2 Months", "10 Years and 6 Months"],
    "Total_EMI_per_month": [5000, 12000],
    "Amount_invested_monthly": [2000, 5000],
    "Payment_Behaviour": ["High_spent_Small_value_payments", "Low_spent_Large_value_payments"],
    "Monthly_Balance": [15000, 20000]
}

df = pd.DataFrame(data)
df.to_csv("data/sample_test.csv", index=False)
df.head()
