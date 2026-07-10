from fastapi import FastAPI
from api.routes.predict import router


app = FastAPI(title='Lead Conversion Prediction API',
              description="Three API's for three differenet stages of lead to predict the conversion and decide the lead score",
              version='1.0')

app.include_router(router)

@app.get("/")

def home():
    return{'message':'WELCOME, Lead Conversion Prediction API',
           'status':'running...'}