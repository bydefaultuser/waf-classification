import pandas as pd
import numpy as np
from faker import Faker

def generate_waf_logs(num_samples=1000):
    fake = Faker()
    data = {
        "Alert ID": [f"ALERT_{i}" for i in range(num_samples)],
        "Timestamp": pd.date_range(start="2023-01-01", periods=num_samples, freq="T"),
        "Source IP": [fake.ipv4() for _ in range(num_samples)],
        "Target URL": [fake.url() for _ in range(num_samples)],
        "Alert Type": np.random.choice(["SQLi", "XSS", "LFI", "RCE"], num_samples),
        "Rule Triggered": np.random.choice(["Rule_1", "Rule_2", "Rule_3"], num_samples),
        "HTTP Parameters": [fake.text(max_nb_chars=50) for _ in range(num_samples)],
        "User-Agent": [fake.user_agent() for _ in range(num_samples)],
        "Status Code": np.random.choice([200, 403, 404, 500], num_samples),
        "Source IP Geolocation": [fake.country() for _ in range(num_samples)],
        "Attack Type Subset": np.random.choice(["Blind SQLi", "Stored XSS"], num_samples),
        "Number of Source IPs": np.random.randint(1, 10, num_samples),
        "Number of Browsers": np.random.randint(1, 5, num_samples),
        "Incident Duration": np.random.randint(1, 60, num_samples),  # in seconds
        "Label": np.random.choice(["FP", "TP"], num_samples, p=[0.7, 0.3]),  # 70% FP, 30% TP
        "Reason": [fake.sentence() if label == "FP" else "" for label in np.random.choice(["FP", "TP"], num_samples)]
    }
    return pd.DataFrame(data)

# Save synthetic data
df = generate_waf_logs(1000)
df.to_csv("data/generated/waf_logs_synthetic.csv", index=False)