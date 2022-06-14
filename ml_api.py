from dataclasses import dataclass
from fastapi import FastAPI,Request
import mlflow
import pandas as pd
from pydantic import Json

mlflow.set_tracking_uri("http://localhost:8118")

app = FastAPI()

@dataclass
class Model:
    '''
    init model from mlflow registry by name and syage
    '''
    model_name:str = None
    model_stage:str = None

    def __post_init__(self):
        self.model = mlflow.pyfunc.load_model(f'models:/{self.model_name}/{self.model_stage}')

    def predict(self,data):
        '''
        predict from data
        '''
        return self.model.predict(data)


model = Model(model_name='dvc_test-elastic_movie_score_pred',model_stage='latest')

@app.post('/invocations')
async def get_predictions(file:Request):

        json_data = await file.json()

        data = pd.read_json(json_data)

        return list(model.predict(data))
