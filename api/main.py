from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd
from pathlib import Path
import sklearn, numpy, scipy

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "model.pkl"

print("Lib versions -> sklearn:", sklearn.__version__, " numpy:", numpy.__version__, " scipy:", scipy.__version__)


# Define the expected input schema using Pydantic
class CKDInput(BaseModel):
    age: float
    bp: float
    sg: float
    al: float
    su: float
    rbc: str
    pc: str
    pcc: str
    ba: str
    bgr: float
    bu: float
    sc: float
    sod: float
    pot: float
    hemo: float
    pcv: int
    wc: int
    rc: float
    htn: str
    dm: str
    cad: str
    appet: str
    pe: str
    ane: str

# Initialize app and load model at startup
app = FastAPI(title="CKD Prediction API")

# Load the trained model from pickle file (and any preprocessors if needed)
with open(MODEL_PATH, "rb") as f:
    pipe = pickle.load(f)

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict_ckd(data: CKDInput):
    df = pd.DataFrame([data.dict()])
    try:
        pred = pipe.predict(df)[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Inference error: {repr(e)}")
    return {"prediction": str(pred)}