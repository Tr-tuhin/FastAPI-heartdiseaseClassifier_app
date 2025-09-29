# app/schemas.py

from pydantic import BaseModel
from typing import List, Optional

# Input schema for /predict
class HeartInput(BaseModel):
    age: float
    sex: int          # 1 = male, 0 = female
    cp: int           # chest pain type
    trestbps: float   # resting blood pressure
    chol: float       # serum cholesterol
    fbs: int          # fasting blood sugar
    restecg: int      # resting ECG results
    thalach: float    # maximum heart rate achieved
    exang: int        # exercise induced angina
    oldpeak: float    # ST depression induced by exercise
    slope: int        # slope of the peak exercise ST segment
    ca: int           # number of major vessels (0–3)
    thal: int         # thalassemia

# Output schema for /predict
class PredictionOutput(BaseModel):
    heart_disease: bool
    probabilities: Optional[List[float]] = None
