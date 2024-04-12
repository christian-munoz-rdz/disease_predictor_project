from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import datetime

app = FastAPI()

logged_in_user = None

# Lista de orígenes permitidos
origins = [
    "http://localhost:8080",  # Permitir solicitudes desde su frontend VueJS
    "http://localhost:3000",
    "http://192.168.1.69:8080",
    "http://192.168.100.17:8080"
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

        # Guardar en la BD
        save_prediction_to_db(prediction)
        
        # Devolver la probabilidad directamente
        return {"probability": float(prediction.flatten()[0]) * 100}
    except Exception as e:
        #raise HTTPException(status_code=500, detail=str(e))
        return {"error":str(e)}

def save_prediction_to_db(prediction: np.ndarray):
    global logged_in_user
    try:
        conexion = mysql.connector.connect(user='sql3696593', password='NMQnIqkJs9',
                                        host='sql3.freesqldatabase.com',
                                        database='sql3696593',
                                        port='3306')
        cursor = conexion.cursor()

        # Insertar datos en la tabla HISTORY
        query = "INSERT INTO `HISTORY` (prediction_probability, prediction_date, username) VALUES (%s, %s, %s)"
        cursor.execute(query, (float(prediction.flatten()[0]), datetime.datetime.now(), logged_in_user))
        conexion.commit()

    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail=f"Error al conectar a la base de datos: {error}")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()


class User(BaseModel):
    username: str
    password: str

@app.post("/login/")
async def login(user: User):
    global logged_in_user
    try:
        conexion = mysql.connector.connect(user='sql3696593', password='NMQnIqkJs9',
                                        host='sql3.freesqldatabase.com',
                                        database='sql3696593',
                                        port='3306')
        cursor = conexion.cursor()

        #Consulta para verificar las credenciales del usuario
        query = "SELECT * FROM `USERS` WHERE username = %s AND passwd = %s"
        cursor.execute(query, (user.username, user.password))
        result = cursor.fetchone()

        #Si las credenciales son válidas, retornar éxito
        if result:
            logged_in_user = user.username
            return {"message": "Login exitoso", "username":user.username}
        else:
            raise HTTPException(status_code=401, detail="Credenciales incorrectas")
        
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail=f"Error al conectar a la base de datos: {error}")
    finally:
        #Cerrar la conexión a la BD
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()


class UserRegistration(BaseModel):
    username: str
    password: str

@app.post("/register/")
async def register_user(user_data: UserRegistration):
    try:
        conexion = mysql.connector.connect(user='sql3696593', password='NMQnIqkJs9',
                                        host='sql3.freesqldatabase.com',
                                        database='sql3696593',
                                        port='3306')
        cursor = conexion.cursor()

        query = "INSERT INTO `USERS` VALUES (NULL, %s, %s);"
        cursor.execute(query, (user_data.username, user_data.password))
        conexion.commit()

        return {"message": "Usuario registrado exitosamente"}
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail=f"Error al conectar a la base de datos: {error}")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

@app.get("/history/")
async def get_history():
    global logged_in_user
    try:
        conexion = mysql.connector.connect(user='sql3696593', password='NMQnIqkJs9',
                                        host='sql3.freesqldatabase.com',
                                        database='sql3696593',
                                        port='3306')
        cursor = conexion.cursor()

        query = "SELECT prediction_date, prediction_probability FROM `HISTORY` WHERE username = %s"
        cursor.execute(query, (logged_in_user,))

        history_entries = cursor.fetchall()

        cursor.close()
        conexion.close()

        return history_entries
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail=f"Error al obtener el historial de consultas: {error}")