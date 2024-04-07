from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import *

app = FastAPI()

class User(BaseModel):
    username: str
    passwd: str

@app.post("/login")
def login(user: User):
    try:
        cone=CConexion.ConexionBD()
        cursor = cone.cursor()
        sql="SELECT FROM USERS WHERE username = %s"
        cursor.execute(sql,(user.username,))
        result = cursor.fetchone()
        cone.close()

        if result and result[2] == user.passwd:
            return {"message": "Inicio de sesión exitoso"}
        else:
            raise HTTPException(status_code=401, detail="Credenciales incorrectas")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def registerUser(username,passwd):
    try:
        cone=CConexion.ConexionBD()
        cursor = cone.cursor()
        sql="INSERT INTO `USERS` VALUES (NULL, %s, %s);"
        valores=(username,passwd)
        cursor.execute(sql,valores)
        cone.commit()
        print(cursor.rowcount,"Registro realizado")
        cone.close()

    except mysql.connector.Error as error:
        print("Error de ingreso de datos {}".format(error))


@app.post("/users/")
async def add_user(username: str, passwd: int):
    user_id = create_user(username, passwd)
    if user_id:
        return {"id": user_id, "name": name, "age": age}
    else:
        raise HTTPException(status_code=400, detail="User not created")
