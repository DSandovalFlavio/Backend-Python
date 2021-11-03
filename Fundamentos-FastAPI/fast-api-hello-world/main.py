#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body

app = FastAPI() # create an instance of FastAPI


# Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None # Optional field
    is_married: Optional[bool] = None # Optional field


@app.get("/")   # path operation decorator con method GET
def home():
    return {"message": "Hello World"} # return a dictionary-Json
# explicacion -> uvicorn main:app --reload
# uvicorn -> es el servidor de python
# main:app -> es el nombre del modulo que contiene la app
# --reload -> es para que se actualice el servidor cada vez que se modifique el codigo

# Request and Response Body

@app.post("/person/new")
def create_person(person: Person = Body(...)): # Body(...) -> es para que el body de la peticion sea un objeto de la clase Person y los 3... que es obligatorio
    return person.dict()
