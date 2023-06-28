from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os
import uvicorn
# Cargar el modelo
modelo = joblib.load('model_rf_GSearch.joblib')

# Definir la estructura de los datos de entrada
class DatosEntrada(BaseModel):
    features: list[float]
    
# Crear la instancia de la aplicación FastAPI
app = FastAPI()

# Definir la ruta y el método para verificar si la aplicación está en funcionamiento
@app.get("/")
def alive():
    return 'Alive'

# Definir la ruta y el método para hacer predicciones
@app.post("/predict")
def predict(data: DatosEntrada):
    # Convertir los datos de entrada en un array de NumPy
    input_data = np.array([data.features], dtype=np.float32)

    # Realizar la predicción utilizando el modelo cargado
    prediction = modelo.predict(input_data)

    # Devolver la predicción como resultado
    return {"prediction": prediction[0]}

# Iniciar el servidor de desarrollo con Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, port=8000)