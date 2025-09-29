import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset (make sure you have data/heart.csv in your repo)
data_path = ".\data\heart.csv"
df = pd.read_csv(data_path)

# Features and target
X = df.drop(columns=["target"])  # assumes "target" column exists
y = df["target"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model along with metadata
os.makedirs("model", exist_ok=True)
joblib.dump(
    {
        "model": model,
        "features": list(X.columns),
        "model_type": "RandomForestClassifier",
    },
    "model/heart_model.joblib"
)

print("Heart Disease model trained and saved successfully → model/heart_model.joblib")
