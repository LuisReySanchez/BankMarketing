from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def alive():
    return 'Alive'