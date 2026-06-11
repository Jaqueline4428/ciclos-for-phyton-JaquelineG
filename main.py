from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

# Crear aplicación FastAPI
app = FastAPI()

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Archivo donde se guardarán las tareas
ARCHIVO = "tareas.txt"

# Modelo de datos
class Tarea(BaseModel):
    nombre: str
    fecha: str

# GUARDAR TAREA
@app.post("/tareas")
def guardar_tarea(tarea: Tarea):

    id_nuevo = 1

    if os.path.exists(ARCHIVO):

        with open(ARCHIVO, "r", encoding="utf8") as f:
            lineas = f.readlines()

            if lineas:
                ultima_linea = lineas[-1].strip()

                if ultima_linea:
                    ultimo = ultima_linea.split("|")
                    id_nuevo = int(ultimo[0]) + 1

    with open(ARCHIVO, "a", encoding="utf8") as f:

        f.write(
            f"{id_nuevo}|{tarea.nombre}|{tarea.fecha}\n"
        )

    return {
        "mensaje": "Guardado correctamente",
        "id": id_nuevo
    }

# OBTENER TAREAS
@app.get("/tareas")
def obtener_tareas():

    datos = []

    if os.path.exists(ARCHIVO):

        with open(ARCHIVO, "r", encoding="utf8") as f:

            for linea in f:

                linea = linea.strip()

                if linea:

                    partes = linea.split("|")

                    if len(partes) == 3:

                        datos.append({
                            "id": int(partes[0]),
                            "nombre": partes[1],
                            "fecha": partes[2]
                        })

    return datos