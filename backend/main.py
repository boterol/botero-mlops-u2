import pickle
from typing import Union
from fastapi import FastAPI, UploadFile, File
import pandas as pd
import DataReformatting 
import DataPreparation
import re

app = FastAPI()


@app.get("/")

def read_root():

    return {"Hello": "World"}

@app.post("/predict_one")
async def predict_one(file: UploadFile = File(...)):
    #se usan los nombres de los archivsod para simular la prediccion de un modelo
    filename=file.filename
    if filename.startswith('_1'):
        return {'TUMOR GRADE: ', 1}
    elif filename.startswith('_2'):
        return {'TUMOR GRADE: ', 2}
    elif filename.startswith('_3'):          
        return {'TUMOR GRADE: ', 3}
    elif filename.startswith('_4'):
        return {'TUMOR GRADE: ', 4}
    
    
    #APLICADO AL PROYECTO DE GRADO

    #df=pd.read_csv(file.file)
    #print(df.head())    
    
    #df=DataReformatting.process(df)
    
    #df=DataPreparation.process(df)

    #print(df.head())
    #with open('decision_tree_model.pkl', 'rb') as f:
    #    clf_model = pickle.load(f)

    #pred=clf_model.predict(df)
    #print('PRED: ', pred)
    #return {'HIGHGRADE: ', pred.tolist()[0]}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):

    return {"item_id": item_id, "q": q}

