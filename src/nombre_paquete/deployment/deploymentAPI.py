from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import joblib
import numpy as np
import logging

# Estructura de los datos
class ApiInput(BaseModel):
    features: List[float]

class ApiOutput(BaseModel):
    is_deposito: List[int]
        
# Instancia de la aplicación FastAPI
app = FastAPI()

# Carga del modelo
modelo = joblib.load('model_rf_GSearch.joblib')

# Configurar el logger
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Raiz
@app.get("/")
def alive():
    return 'Alive'

# Definir la ruta y el método para hacer predicciones
@app.post("/predict")
async def create_user(data: ApiInput) -> ApiOutput:

    try:
        input_data = np.array(data.features).reshape(1,20)
        prediction = modelo.predict(input_data).flatten().tolist()
        preds=ApiOutput(is_deposito=prediction)

        return preds
    
    except Exception as e:
        logger.error(f"Error durante la predicción: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")
        print("error: ",e)
        
