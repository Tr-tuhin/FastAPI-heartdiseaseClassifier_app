from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import HeartInput, PredictionOutput
import joblib
import numpy as np

# Load model
model = joblib.load("model/heart_model.joblib")

# Create FastAPI app
app = FastAPI(
    title="Heart Disease Predictor",
    description="Predicts heart disease using FastAPI",
    version="1.0"
) 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "API is running"}

@app.post("/predict", response_model=PredictionOutput)
def predict_heart(data: HeartInput):
    features = np.array([[data.age, data.sex, data.cp, data.trestbps,
                          data.chol, data.fbs, data.restecg,
                          data.thalach, data.exang, data.oldpeak,
                          data.slope, data.ca, data.thal]])
    prediction = model.predict(features)[0]
    return {"predicted_class": int(prediction)}
