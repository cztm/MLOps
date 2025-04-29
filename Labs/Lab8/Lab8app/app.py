# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.sklearn
import uvicorn

mlflow.set_tracking_uri('sqlite:///mlflow.db')


# Load the MLflow model
model = mlflow.sklearn.load_model("models:/Lab8_model/4")

# Create FastAPI app
app = FastAPI()

# Define a "friendly" input format
class FriendlyPredictionRequest(BaseModel):
    gender: str  # "Male" or "Female"
    marital_status: str  # "Yes" or "No"
    anxiety: str  # "Yes" or "No"
    panic_attack: str  # "Yes" or "No"
    sought_specialist: str  # "Yes" or "No"

# Friendly output mapping
label_mapping = {
    0: "Not at Risk of Depression",
    1: "At Risk of Depression"
}

# Prediction endpoint
@app.post("/predict")
def predict(request: FriendlyPredictionRequest):
    # Map friendly input into numbers
    gender = 1 if request.gender == "Male" else 0
    marital_status = 1 if request.marital_status == "Yes" else 0
    anxiety = 1 if request.anxiety == "Yes" else 0
    panic_attack = 1 if request.panic_attack == "Yes" else 0
    sought_specialist = 1 if request.sought_specialist == "Yes" else 0

    # Build the model input
    model_input = [[gender, marital_status, anxiety, panic_attack, sought_specialist, 0, 0]]

    # Predict
    preds = model.predict(model_input)
    friendly_preds = [label_mapping[pred] for pred in preds]
    return {"predictions": friendly_preds}

# Run server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

