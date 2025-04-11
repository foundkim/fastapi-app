"""Inference Schemas module"""

from pydantic import BaseModel


class InferenceIn(BaseModel):
    """Model for inference request"""

    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class InferenceOut(BaseModel):
    """Inference output"""

    prediction: float
