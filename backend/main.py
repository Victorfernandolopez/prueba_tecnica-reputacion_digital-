from fastapi import FastAPI #importacion de fastapi
from fastapi.responses import JSONResponse #importacion de JSONResponse para respuestas personalizadas
from fastapi.staticfiles import StaticFiles #importacion de StaticFiles para servir archivos estaticos
import os #importacion de os para manejar rutas de archivos

import json
from pathlib import Path # importamos Path para manejar rutas de archivos



# creamos una instancia de FastAPI
app = FastAPI()

# servimos los archivos estáticos del frontend
app.mount("/", StaticFiles(directory=Path(__file__).parent / "static", html=True), name="static")

@app.get("/data")# este decorador permite definir una ruta para la api al utilizar el metodo get

def get_data():
    # si existe en /data.json (para Docker)
    if Path("/data.json").exists():
        data_file = Path("/data.json")
    else:
        # Si no,se usá el que está al lado de main.py (para desarrollo en ese caso copiar el archivo en la carpeta backend)
        data_file = Path(__file__).parent / "data.json"

    #verificacion para ver si el archivo existe
    if data_file.exists():
        #si existe, lo abrimos y cargamos su contenido
        with data_file.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return JSONResponse(content=data)
    else:
        #si no existe, devolvemos un error 404
        return JSONResponse(status_code=404, content={"error": "data.json no encontrado"})
