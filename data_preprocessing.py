import pandas as pd
import numpy as np

# Load dataset (GST transactions, tax records, etc.)
df = pd.read_csv("financial_transactions.csv")

# Remove missing values
df_clean = df.dropna()

# Convert transaction amount to logarithmic scale
df_clean['amount_log'] = df_clean['transaction_amount'].apply(lambda x: np.log(x + 1))

# Feature engineering (creating risk factors)
df_clean['risk_score'] = (df_clean['amount_log'] * 0.7) + (df_clean['transaction_type'] * 0.3)

# Save processed dataset
df_clean.to_csv("clean_financial_data.csv", index=False)

print("✅ Data Preprocessing Completed!")
