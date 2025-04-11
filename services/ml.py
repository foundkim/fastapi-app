"""ML Service"""

import pandas as pd
import mlflow

from schemas import InferenceIn

from core import config


model = mlflow.pyfunc.load_model(model_uri=config.MODEL_URI)


def get_prediction(input: InferenceIn) -> float:
    """Get prediction from data"""

    predict = pd.DataFrame(input.model_dump(mode="python"))

    return model.predict(predict[0])
