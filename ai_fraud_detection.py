from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load preprocessed data
df = pd.read_csv("clean_financial_data.csv")

# Features and labels
X = df[['amount_log', 'transaction_type', 'account_balance']]
y = df['fraud_flag']  # 0 = Legit, 1 = Fraud

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save trained model
joblib.dump(model, "fraud_detection_model.pkl")

print("✅ AI Fraud Detection Model Trained & Saved!")
