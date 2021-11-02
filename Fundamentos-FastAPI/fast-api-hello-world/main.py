from fastapi import FastAPI

app = FastAPI() # create an instance of FastAPI

@app.get("/")   # path operation decorator con method GET
def home():
    return {"message": "Hello World"} # return a dictionary-Json


# explicacion -> uvicorn main:app --reload
# uvicorn -> es el servidor de python
# main:app -> es el nombre del modulo que contiene la app
# --reload -> es para que se actualice el servidor cada vez que se modifique el codigo
