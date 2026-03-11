from fastapi import FastAPI
import pandas as pd
import pickle

app = FastAPI()

data_store = []

model = pickle.load(open("ml/model.pkl","rb"))

@app.post("/sensor")

def receive_data(data: dict):

    data_store.append(data)

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    return {
        "prediction": int(prediction)
    }

@app.get("/data")

def get_data():
    return data_store