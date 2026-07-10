import pandas as pd
from api.config import models,thresholds

def predict(model_type:str,data:dict):
    model = models[model_type]
    threshold = thresholds[model_type]

    df = pd.DataFrame([data])

    probability = model.predict_proba(df)[0][1]

    prediction = int(probability>=threshold)

    return {'prediction':prediction,
            'probability':round(float(probability),2),
            'threshold':threshold}