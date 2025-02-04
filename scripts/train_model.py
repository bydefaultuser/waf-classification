import pandas as pd
from xgboost import XGBClassifier
import joblib

# Load processed data
df = pd.read_csv("data/processed/waf_logs_processed.csv")
X = df.drop(columns=["Label", "Reason", "Alert ID"])
y = df["Label"]

# Train final model
model = XGBClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "models/waf_classifier.pkl")