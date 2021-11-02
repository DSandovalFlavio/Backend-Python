# ¿Que es FastAPI?

El framework mas veloz para el desarrollo web con Python. Enfocado para realizar APIs, es el mas rápido en lo que respecta a la velocidad del servidor superando a Node.Js y a GO. Fue creado por Sebastian Ramirez, es de código abierto y se encuentra en Github, es usado por empresas como Uber, Windows, Netflix y Office.

Documentación: https://fastapi.tiangolo.com

Código Fuente: https://github.com/tiangolo/fastapi

# Ubicación de FastAPI en el ecosistema de Python

FastAPI utiliza otros frameworks dentro de si para funcionar

- Uvicorn: es una librería de Python que funciona de servidor, es decir, permite que cualquier computadora se convierta en un servidor.
- Starlette: es un framework de desarrollo web de bajo nivel, para desarrollar aplicaciones con este requieres un amplio conocimiento de Python, entonces FastAPI se encarga de añadirle funcionalidades por encima para que se pueda usar mas fácilmente.
- Pydantic: Es un framework que permite trabajar con datos similar a pandas, pero este te permite usar modelos los cuales aprovechara FastAPI para crear la API.

# Path Operations

Path: Es una routa (route o endpoint) la cual nosotros ingresamos seguido el dominio de nuestro aplicativo.

127.0.0.1:8000 -> myproject.com/API/
                    
                    Diminio/Path ->

Operation: Es un metodo http por el cual nos comunicamos. 

Metodo:

- Head
- Patch

Options:

- Get: Obtener
- Post: Crear
- Put: Modificar/Actualizar
- Delete: Eliminar

Path Operations -> Utilizando Metodos y Options

# Path Operation Decorator

~~~python
@app.get("/") # Primera parte
def home(): # Segunda parte
    return {"message": "Hello World"}
~~~

*Primera parte (Path Operator Decorator)* : permite el ingreso de una path a una operation designada para la ejecucion de un codigo.

*Segunda parte (Path Operation Function)* : realiza la ejecucion de un codigo siguiendo la especificación del path operation decorator llamado anteriormente