# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** Predicción de un préstamo a largo basado en modelo de Random Forest.
- **Plataforma de despliegue:** El modelo será desplegado en un servidor local usando ngrok como método de apretura de puertos.
- **Requisitos técnicos:** 
    - *versión de Python:* Python 3.10.2
    - *Librerias:* fastapi(0.98.0), numpy(1.22.3), uvicorn(0.22.0), pandas (1.4.1) , matplotlib (3.5.1), scikit-learn (1.0.2)
    - *Software:* Linux base OS (Manjaro Linux X86_64), kernel 6.1.31-MANJARO
    - *Hardware:* CPU: AMD Ryzen 5 5600X (12) @ 4.200GHz, GPU: NVIDIA GeForce RTX 3060, RAM: 31976 MiB
- **Requisitos de seguridad:** Los datos proviene de una institución bancaria portuguesa los cuales fueron previamente anonimizados por lo que no es necesaria la encriptación

- **Diagrama de arquitectura:**

![Modelo Arquitectura](https://www.bbvaapimarket.com/wp-content/uploads/2016/04/cibbva_modelo.png)

## Código de despliegue

- **Archivo principal:** La aplicación diseñada está en el archivo *deploymentAPIs.ipynb*
- **Rutas de acceso a los archivos:** El código puede encontrarse en *'src/nombre_paquete/deployment/deploymentAPI.ipynb'*

## Documentación del despliegue

- **Instrucciones de instalación:** Debe considerar la instalación de los paquetes asociados a openslide como a NVIDIA (CUDA, CUDNN). El resto de librerías mencionadas puede obtenerse por medio de pip. 
- **Instrucciones de configuración:** La mayoría de hiperparametros del modelo han sido explorados previamente y por consiguiente no se recomienda ninguna modificación sobre estos.
- **Instrucciones de uso:** El despliegue del modelo consta de dos pasos
    - *Despliegue del servidor:* Se pone en producción la aplicación creada, para ello ejecutar.
          - uvicorn {main_file_path}:app --reload 
    - *Apertura de puertos:* Para poder tener acceso a nuestro servicio desde cualquier punto debemos abrir el 8000, no obstante esto se encuentran normalmente restringidos por nuestro operado de internet, para evadir dichas limitaciones usamos el servicio de ngrok.
          - ./MLDS6project/src/nombre_paquete/preprocessing/ngrok http 8000
