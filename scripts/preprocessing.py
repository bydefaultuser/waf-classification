import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

def preprocess_data(df):
    # Convert 'Timestamp' column to datetime
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])

    # Extract datetime features
    df["Hour"] = df["Timestamp"].dt.hour
    df["Day of Week"] = df["Timestamp"].dt.dayofweek

    # Encode categorical features using OneHotEncoder
    categorical_cols = ["Source IP", "Target URL", "Alert Type", "Rule Triggered", "HTTP Parameters", 
                        "User-Agent", "Source IP Geolocation", "Attack Type Subset"]
    encoder = OneHotEncoder(sparse=False, handle_unknown="ignore")
    encoded_features = encoder.fit_transform(df[categorical_cols])
    encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_cols))

    # Convert labels to numerical values (FP -> 0, TP -> 1)
    df["Label"] = df["Label"].map({"FP": 0, "TP": 1})

    # Drop original columns and concatenate encoded ones
    df = df.drop(columns=categorical_cols + ["Timestamp"])
    df = pd.concat([df, encoded_df], axis=1)

    return df

# Load and preprocess data
df = pd.read_csv("data/generated/waf_logs_synthetic.csv")
df_processed = preprocess_data(df)
df_processed.to_csv("data/processed/waf_logs_processed.csv", index=False)