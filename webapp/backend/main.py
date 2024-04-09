from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Lista de orígenes permitidos
origins = [
    "http://localhost:8080",  # Permitir solicitudes desde su frontend VueJS
    "http://localhost:3000",
    "http://192.168.1.69:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Los orígenes que queremos permitir
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Clase para los datos de entrada
class DiabetesData(BaseModel):
    # Asegúrese de que los nombres y tipos de datos coincidan con lo que su modelo espera
    pregnancies: int
    glucose: float
    bloodPressure: float
    skinThickness: float
    insulin: float
    bmi: float
    diabetesPedigreeFunction: float
    age: int

# Cargar el modelo de TensorFlow
model = tf.keras.models.load_model("model.h5")

# Cargar el dataset para el scaler (esto es sólo un ejemplo, ajuste según sea necesario)
df = pd.read_csv("diabetes.csv")
X = df.iloc[:, :-1].values
scaler = StandardScaler().fit(X)

@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.post("/predict/")
async def predict(data: DiabetesData):
    try:
        print("Recibido")
        # Convertir datos de entrada a DataFrame para escalar
        data_df = pd.DataFrame([data.dict().values()], columns=data.dict().keys())
        scaled_data = scaler.transform(data_df)
        
        # Realizar predicción
        prediction = model.predict(scaled_data)
        
        # Devolver la probabilidad directamente
        return {"probability": float(prediction.flatten()[0]) * 100}
    except Exception as e:
        #raise HTTPException(status_code=500, detail=str(e))
        return {"error":str(e)}

