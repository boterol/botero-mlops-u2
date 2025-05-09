import pickle

from typing import Union

from fastapi import FastAPI, UploadFile, File

import pandas as pd

import DataReformatting 
import DataPreparation

app = FastAPI()


@app.get("/")

def read_root():

    return {"Hello": "World"}

@app.post("/predict_one")
async def predict_one(file: UploadFile = File(...)):
    df=pd.read_csv(file.file)
    print(df.head())    
    
    df=DataReformatting.process(df)
    
    df=DataPreparation.process(df)

    print(df.head())
    with open('decision_tree_model.pkl', 'rb') as f:
        clf_model = pickle.load(f)

    pred=clf_model.predict(df)
    print('PRED: ', pred)
    return {'HIGHGRADE: ', pred.tolist()[0]}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):

    return {"item_id": item_id, "q": q}

