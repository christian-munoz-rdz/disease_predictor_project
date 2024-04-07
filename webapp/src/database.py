import mysql.connector

class CConexion:

  def ConexionBD():
    try:
        conexion = mysql.connector.connect(user='sql3696593', password='NMQnIqkJs9',
                                        host='sql3.freesqldatabase.com',
                                        database='sql3696593',
                                        port='3306')
        print("Conexion correcta")

        return conexion

    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos {}".format(error))

        return conexion
  ConexionBD()
"""from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")

# Connect to MySQL
def connect():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )

def create_user(username, passwd):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO USERS (username, passwd) VALUES (%s, %s)"
    values = (username, passwd)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return cursor.lastrowid

# ... [other CRUD functions]
"""