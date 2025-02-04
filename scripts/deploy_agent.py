from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load trained model
model = joblib.load("models/waf_classifier.pkl")

@app.post("/classify")
async def classify(log: dict):
    # Convert log to DataFrame
    df = pd.DataFrame([log])
    # Preprocess (ensure this matches training preprocessing)
    df = preprocess_data(df)
    # Predict
    prediction = model.predict(df.drop(columns=["Label", "Reason", "Alert ID"]))
    return {"prediction": prediction[0]}