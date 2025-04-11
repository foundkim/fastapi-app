"""Inference endpoints"""

from fastapi import APIRouter

from schemas import InferenceOut, InferenceIn
from services.ml import get_prediction


inference_router = APIRouter(prefix="/inference", tags=["Prediction",])


@inference_router.post("/", response_model=InferenceOut)
async def predict(input: InferenceIn):
    """Predict"""

    return InferenceOut(prediction= get_prediction(input=input))
