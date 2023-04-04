# table of contents
- [table of contents](#table-of-contents)
- [Introduccion a Fast API](#introduccion-a-fast-api)
- [Introduccion](#introduccion)
  - [Que es fast API](#que-es-fast-api)
  - [Instalacion de Fast API](#instalacion-de-fast-api)
    - [Iniciar servidor uvicorn](#iniciar-servidor-uvicorn)
  - [Documentacion automatica con Swagger](#documentacion-automatica-con-swagger)
  - [Metodos HTTP en FastAPI](#metodos-http-en-fastapi)
  - [Metodo GET](#metodo-get)
  - [Parametros de ruta](#parametros-de-ruta)
  - [Parametros Query](#parametros-query)
  - [Metodo POST](#metodo-post)
  - [Métodos PUT y DELETE](#métodos-put-y-delete)
- [Validaciones con Pydantic](#validaciones-con-pydantic)
  - [Creacion de esquemas](#creacion-de-esquemas)
  - [Validaciones de tipos de datos](#validaciones-de-tipos-de-datos)
  - [Validaciones de parametros](#validaciones-de-parametros)
  - [Tipos de respuestas](#tipos-de-respuestas)
  - [Codigos de estado](#codigos-de-estado)
- [Autenticacion](#autenticacion)
  - [Flujo de autenticacion](#flujo-de-autenticacion)
  - [Generacion de tokens con pyjwt](#generacion-de-tokens-con-pyjwt)
  - [Validacion de tokens](#validacion-de-tokens)
  - [Middlewares de autenticacion](#middlewares-de-autenticacion)
- [Curso de FastAPI: Base de Datos, Modularización y Deploy a Producción](#curso-de-fastapi-base-de-datos-modularización-y-deploy-a-producción)
- [Conexion con bases de datos](#conexion-con-bases-de-datos)
  - [SQLAlchemy: el ORM de FastAPI](#sqlalchemy-el-orm-de-fastapi)
  - [Instalacion y configuracion](#instalacion-y-configuracion)
  - [Creacion de modelos](#creacion-de-modelos)
  - [Registro de datos](#registro-de-datos)
  - [Consulta de datos](#consulta-de-datos)
  - [Modificacion y eliminacion de datos](#modificacion-y-eliminacion-de-datos)
  - [SQLMODEL: El futuro ORM de FastAPI](#sqlmodel-el-futuro-orm-de-fastapi)
- [Modularizacion](#modularizacion)
  - [Manejo de errores y middlewares](#manejo-de-errores-y-middlewares)
  - [Creacion de routers](#creacion-de-routers)
  - [Servicios para consultar datos](#servicios-para-consultar-datos)
  - [Servicios para registrar o modificar datos](#servicios-para-registrar-o-modificar-datos)
- [Despliegue](#despliegue)
  - [Preparando el proyecto para desplegar a produccion](#preparando-el-proyecto-para-desplegar-a-produccion)
  - [Creando el repositorio en GitLab](#creando-el-repositorio-en-gitlab)
  - [Creando el Droplet en DigitalOcean](#creando-el-droplet-en-digitalocean)
- [Instalacion de herramientas para el servidor](#instalacion-de-herramientas-para-el-servidor)
- [Ejecutando FastAPI con NGINX](#ejecutando-fastapi-con-nginx)


# Introduccion a Fast API
¡FastAPI es el framework más utilizado para desarrollo backend con Python! Crea tu primera API REST usando Path Operations, validación de esquemas y tipado con Pydantic, autenticación con PyJWT y documentación automática con Swagger.

# Introduccion
## Que es fast API
FastAPI es un marco moderno de Python para construir aplicaciones web y APIs de alta velocidad. Utiliza la tipificación de variables y la asincronía para mejorar la eficiencia del código, y permite una fácil documentación automática de la API. Además, es compatible con OpenAPI (anteriormente conocido como Swagger), lo que permite a los desarrolladores integrar su API con otras herramientas y servicios de terceros que admiten la especificación OpenAPI. Aquí está un ejemplo básico de cómo se vería una aplicación FastAPI que devuelve un objeto JSON:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

En este ejemplo, se inicia una aplicación FastAPI y se define una ruta / para el método HTTP GET. El decorador @app.get("/") indica al framework la ruta que se está definiendo y el método HTTP asociado. La función root devuelve un objeto JSON con el mensaje "Hello World".

1. [Clase](https://platzi.com/clases/5354-fastapi/57712-que-es-fastapi/)

## Instalacion de Fast API

1. [Clase](https://platzi.com/clases/5354-fastapi/57713-instalacion-de-fastapi-y-creacion-de-tu-primera-ap/)

### Iniciar servidor uvicorn

Para iniciar un servidor uvicorn que se actualice automáticamente en un puerto específico al que se pueda acceder desde cualquier dispositivo en su red, siga los siguientes pasos:

1. Instale el paquete uvicorn y fastapi usando el comando pip:
   
```
pip install fastapi uvicorn
```

2. Crea un archivo main.py con el siguiente contenido:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
3. En el código anterior, el servidor se ejecuta en el puerto 8000 y está disponible en cualquier dispositivo en su red local. El argumento host se establece en 0.0.0.0 para que la aplicación sea accesible desde cualquier dirección IP.

4. Ejecute el servidor usando el siguiente comando:

```
uvicorn main:app --reload
```
El parámetro --reload le permitirá actualizar el servidor automáticamente cuando detecte cambios en el código fuente.

5. Ahora puede acceder a su servidor en cualquier dispositivo dentro de su red local usando la dirección IP de la máquina que ejecuta el servidor y el puerto 8000. Por ejemplo, si la dirección IP de su máquina es 192.168.0.10, abra un navegador web y vaya a http://192.168.0.10:8000.

## Documentacion automatica con Swagger
1. [Clase](https://platzi.com/clases/5354-fastapi/57714-documentacion-automatica-con-swagger/)

```
http://localhost:8000/docs.
```

```python
from fastapi import FastAPI

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"

@app.get("/", tags=['home'])
def message():
    return "Hello World"
```
## Metodos HTTP en FastAPI
1. [Documentacion](https://platzi.com/clases/5354-fastapi/57737-metodos-http-en-fastapi/)

## Metodo GET
1. [Clase](https://platzi.com/clases/5354-fastapi/57715-metodo-get/)
   
```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"

movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]

@app.get("/", tags=['home'])
def message():
    return HTMLResponse('<h1>¡Hola mundo!</h1>')

@app.get("/movies", tags=['movies'])
def get_movies():
    return movies
```
## Parametros de ruta 
1. [Clase](https://platzi.com/clases/5354-fastapi/57716-parametros-de-ruta/)

```python
@app.get("/movies/{id}", tags=['movies'])
def get_movie(id: int):
    for item in movies:
        if item['id'] == id:
            return item
    return []
```
## Parametros Query
1. [Clase](https://platzi.com/clases/5354-fastapi/57717-parametros-query/)

```python
@app.get("/movies/", tags=['movies'])
def get_movies_by_category(category: str, year: int):
    return [item for item in movies if item['category'] == category]
```

## Metodo POST
1. [Clase](https://platzi.com/clases/5354-fastapi/57718-metodo-post/)

```python
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	},
    {
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]

@app.post("/movies", tags=['movies'])
def create_movie(id: int =  Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    movie = {
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    }
    movies.append(movie)
    return movies
```
## Métodos PUT y DELETE
1. [Clase](https://platzi.com/clases/5354-fastapi/57719-metodos-put-y-delete/)

```python
@app.put("/movies/{id}", tags=['movies'])
def update_movie(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    for item in movies:
        if item['id'] == id:
            item['title'] = title
            item['overview'] = overview
            item['year'] = year
            item['rating'] = rating
            item['category'] = category
            return item
    return movies

@app.delete("/movies/{id}", tags=['movies'])
def delete_movie(id: int):
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return movies
```
# Validaciones con Pydantic
## Creacion de esquemas
1. [Clase](https://platzi.com/clases/5354-fastapi/57720-creacion-de-esquemas/)

```python
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from tiping import Optional

...

class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    overview: str
    year: int
    rating: float
    category: str
...

@app.post("/movies", tags=['movies'])
def create_movie(movie: Movie):
    movies.append(movie)
    return movies

@app.put("/movies/{id}", tags=['movies'])
def update_movie(id: int, movie: Movie):
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            return movies
```
## Validaciones de tipos de datos
1. [Clase](https://platzi.com/clases/5354-fastapi/57721-validaciones-de-tipos-de-datos/)

```python
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from tiping import Optional

...

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default = "Mi pelicula", min_length = 5, max_length=15)
    overview: str = Field(min_length = 15, max_length=50)
    year: int = Field(ge = 1900, le = 2021)
    rating: float = Field(ge = 1, le = 10)
    category: str

    class Config: # Valores por defecto
        schema_extra = {
            "example":{
                "id": 1,
                "title": "Mi pelicula",
                "overview": "Descripcion de la pelicula",
                "year": 2021,
                "rating": 7.8,
                "category": "Acción"
            }
        }
```
## Validaciones de parametros
1. [Clase](https://platzi.com/clases/5354-fastapi/57722-validaciones-de-parametros/)

```python
from fastapi import FastAPI, Body, Path, Query

...

@app.get("/movies/{id}", tags=['movies'])
def get_movie(id: int = Path(ge = 1, le = 2000) ):
    for item in movies:
        if item['id'] == id:
            return item
    return []

@app.get("/movies/", tags=['movies'])
def get_movies_by_category(category: str = Query(min_lenght = 5, max_length = 10)):
    return [item for item in movies if item['category'] == category]
```

## Tipos de respuestas
1. [Clase](https://platzi.com/clases/5354-fastapi/57723-tipos-de-respuestas/)

```python
from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from tiping import Optional, List

... 

@app.get("/movies", tags=['movies'], response_model=List[Movie])
def get_movies() -> List[Movie]:
    return JSONResponse(content=movies)

...

@app.get("/movies/", tags=['movies'], response_model =  List[Movie])
def get_movies_by_category(category: str = Query(min_lenght = 5, max_length = 10)) -> List[Movie]:
    data = [item for item in movies if item['category'] == category]
    return JSONResponse(content = data)

@app.post("/movies", tags=['movies'], response_model = dict)
def create_movie(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(content = {'message': 'Pelicula creada'})
...

```
## Codigos de estado
1. [Clase](https://platzi.com/clases/5354-fastapi/57724-codigos-de-estado/)
2. [Documentacion](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

```python
...
@app.get("/movies", tags=['movies'], response_model=List[Movie], status_code = 200)
def get_movies() -> List[Movie]:
    return JSONResponse(status_code =200, content=movies)

@app.get("/movies/{id}", tags=['movies'], response_model = Movie)
def get_movie(id: int = Path(ge = 1, le = 2000)) -> Movie:
    for item in movies:
        if item['id'] == id:
            return JSONResponse(content = item)
    return JSONResponse(status_code = 404, content = {'message': 'No se encontró la pelicula'})
...

@app.post("/movies", tags=['movies'], response_model = dict, status_code = 201)
def create_movie(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(status_code = 201, content = {'message': 'Pelicula creada'})
...
```

# Autenticacion
## Flujo de autenticacion 
1. [Documentacion](https://platzi.com/clases/5354-fastapi/57738-flujo-de-autenticacion/)

## Generacion de tokens con pyjwt
1. [Clase](https://platzi.com/clases/5354-fastapi/57725-generando-tokens-con-pyjwt/)

```
pip install pyjwt
```

```python
from jwt import encode

def create_token(data: dict):
    token: str = encode(payLoad = data, key = "my_secret_key", algorithm = "HS256")
    return token
```

```python
...
from jwt_manager import create_token

...

class User(BaseModel):
    email: str
    password: str

... 

@app.post("/login", tags=['auth'], response_model = dict)
def login(user: User) -> dict:
    token = create_token(data = user.dict())
    return JSONResponse(content = {'token': token})
```
## Validacion de tokens
1. [Clase](https://platzi.com/clases/5354-fastapi/57726-validando-tokens/)

```python
def validate_token(token: str) -> dict:
    data: dict = decode(token, key = "my_secret_key", algorithms = ["HS256"])
    return data
```

```python
@app.post("/login", tags=['auth'], response_model = dict)
def login(user: User) -> dict:
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(data = user.dict())
    return JSONResponse(status_code = 200, content = {'token': token})
```
## Middlewares de autenticacion
1. [Clase](https://platzi.com/clases/5354-fastapi/57727-middlewares-de-autenticacion/)

```python
from fastapi import FastAPI, Body, Path, Query, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from tiping import Optional, List
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer

... 

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Invalid token")

...

@app.post("/login", tags=['auth'], response_model = dict)
def login(user: User) -> dict:
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(data = user.dict())
    return JSONResponse(status_code = 200, content = {'token': token})

@app.get("/movies", tags=['movies'], response_model=List[Movie], status_code = 200, dependencies = [Depends (JWTBearer())])
def get_movies() -> List[Movie]:
    return JSONResponse(status_code =200, content=movies)

...
```

# Curso de FastAPI: Base de Datos, Modularización y Deploy a Producción

¡Conecta tus proyectos de FastAPI a bases de datos relacionales con SQLAlchemist! Modulariza tu proyecto siguiendo las mejores prácticas de organización y escalamiento. Despliega a producción cualquiera proyecto de backend con Python usando GitLab, Digital Ocean y NGNIX.

# Conexion con bases de datos 

## SQLAlchemy: el ORM de FastAPI
1. [Clase](https://platzi.com/clases/5355-fastapi-modularizacion-datos/57739-sqlalchemy-el-orm-de-fastapi/)

**ORM**
ORM significa "Object-Relational Mapping". Es una técnica de programación que permite a los desarrolladores de software interactuar con las bases de datos relacionales utilizando un paradigma orientado a objetos. ORM mapea o convierte los datos de la base de datos en objetos, y viceversa, lo que permite a los desarrolladores trabajar con datos de la base de datos como si fueran objetos en el código. El uso de ORM puede agilizar el desarrollo de aplicaciones y simplificar el acceso y manipulación de datos en la base de datos.

Para utilizar un ORM en Python, se pueden utilizar varias librerías populares como SQLAlchemy, Django ORM, Peewee y Pony ORM, entre otras. A continuación, se presentará un ejemplo básico de cómo utilizar SQLAlchemy para conectarse a una base de datos y realizar operaciones CRUD:

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crear una conexión a la base de datos
db_engine = create_engine('mysql://user:password@localhost/mydatabase')

# Crear una sesión para manejar operaciones con la base de datos
Session = sessionmaker(bind=db_engine)
session = Session()

# Crear una clase para mapear la tabla en la base de datos a un objeto en Python
Base = declarative_base()
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# Crear un nuevo registro en la tabla 'customers'
new_customer = Customer(name='John Doe', age=30)
session.add(new_customer)
session.commit()

# Obtener todos los registros de la tabla 'customers'
customers = session.query(Customer).all()
for customer in customers:
    print(customer.name, customer.age)

# Actualizar un registro en la tabla 'customers'
customer_to_update = session.query(Customer).filter_by(name='John Doe').first()
customer_to_update.age = 31
session.commit()

# Borrar un registro en la tabla 'customers'
customer_to_delete = session.query(Customer).filter_by(name='John Doe').first()
session.delete(customer_to_delete)
session.commit()

```
Este es un ejemplo básico que muestra cómo SQLAlchemy puede utilizarse para interactuar con una base de datos MySQL. Cada ORM tiene su propia sintaxis y forma de trabajar, pero todos siguen el mismo paradigma orientado a objetos que hace que trabajar con bases de datos sea más fácil y eficiente.

## Instalacion y configuracion
1. [Clase](https://platzi.com/clases/5355-fastapi-modularizacion-datos/57740-instalacion-y-configuracion-de-sqlalchemy/)

```python
import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = "database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

engine = create_engine(database_url, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()
```
## Creacion de modelos
1. [Clase](https://platzi.com/clases/5355-fastapi-modularizacion-datos/57741-creacion-de-modelos/)

En la carpeta models
```python
from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Movie(Base):

    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)
```

en el archivo main.py 

```python
...
from config.database import Session, engine, Base
from models.movie import Movie

Base.metadata.create_all(bind=engine)

...
```
Al correr la aplicacion, deberia crear la tabla movies con los campos indicados 

## Registro de datos 
1. [Clase](https://platzi.com/clases/5355-fastapi-modularizacion-datos/57742-registro-de-datos/)

```python
...
from models.movie import Movie as MovieModel

Base.metadata.create_all(bind=engine)

...

@app.post("/movies", tags=['movies'], response_model = dict, status_code = 201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    new_movie = MovieModel(**movie.dict())
    db.add(new_movie)
    db.commit()
    return JSONResponse(status_code = 201, content = {'message': 'Pelicula creada'})
```
## Consulta de datos
1. [Clase](https://platzi.com/clases/5355-fastapi-modularizacion-datos/57743-consulta-de-datos/)

```python
...
from fastapi.encoders import jsonable_encoder

...

@app.get("/movies", tags=['movies'], response_model=List[Movie], status_code = 200, dependencies = [Depends (JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = db.query(MovieModel).all()
    return JSONResponse(status_code =200, content=jsonable_encoder(result))

@app.get("/movies/{id}", tags=['movies'], response_model = Movie)
def get_movie(id: int = Path(ge = 1, le = 2000)) -> Movie:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code = 404, content = {'message': 'No se encontró la pelicula'})
    return JSONResponse(status_code = 200, content = jsonable_encoder(result))

@app.get("/movies/", tags=['movies'], response_model =  List[Movie])
def get_movies_by_category(category: str = Query(min_lenght = 5, max_length = 10)) -> List[Movie]:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.category == category).all()
    return JSONResponse(status_code = 200, content = jsonable_encoder(result))
```
## Modificacion y eliminacion de datos 
1. [Clase](https://platzi.com/clases/5355-fastapi-modularizacion-datos/57744-modificacion-y-eliminacion-de-datos/)

```python
@app.put("/movies/{id}", tags=['movies'], response_model = dict)
def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code = 404, content = {'message': 'No se encontró la pelicula'}) 
    result.title = movie.title
    result.overview = movie.overview
    result.year = movie.year
    result.rating = movie.rating
    result.category = movie.category
    db.commit()
    return JSONResponse(status_code = 200, content = {'message': 'Pelicula actualizada'})

@app.delete("/movies/{id}", tags=['movies'], response_model = dict)
def delete_movie(id: int) -> dict:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code = 404, content = {'message': 'No se encontró la pelicula'})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code = 200, content = {'message': 'Pelicula eliminada'})

```
## SQLMODEL: El futuro ORM de FastAPI
1. [Clase](https://platzi.com/clases/5355-fastapi-modularizacion-datos/57745-sqlmodel-el-futuro-orm-de-fastapi/)

# Modularizacion 
## Manejo de errores y middlewares
1. [Clase](https://platzi.com/clases/5355-fastapi-modularizacion-datos/57746-manejo-de-errores-y-middlewares/)

En la carpeta middlewares

archivo error_handler.py

```python
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI):
        super().__init__(app)

    async def dispatch(self, request, call_next) -> Response | JSONResponse:
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            return JSONResponse(
                status_code=500,
                content={"error": str(e)}
            )
```
archivo jwt_bearer.py

```python
from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from jwt_manager import validate_token

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Invalid token")
```
```python
...
from middlewares.error_handler import ErrorHandler
from middlewares.jwt_bearer import JWTBearer

... 

app.version = "0.0.1"

app.add_middleware(ErrorHandler)
```
## Creacion de routers
1. [Clase](https://platzi.com/clases/5355-fastapi-modularizacion-datos/57747-creacion-de-routers/)

En la carpeta routers en el archivo movies.py

```python
from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
movie_router = APIRouter()

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default = "Mi pelicula", min_length = 5, max_length=15)
    overview: str = Field(min_length = 15, max_length=50)
    year: int = Field(ge = 1900, le = 2021)
    rating: float
    category: str

    class Config: # Valores por defecto
        schema_extra = {
            "example":{
                "id": 1,
                "title": "Mi pelicula",
                "overview": "Descripcion de la pelicula",
                "year": 2021,
                "rating": 7.8,
                "category": "Acción"
            }
        }

@movie_router.get("/movies", tags=['movies'], response_model=List[Movie], status_code = 200, dependencies = [Depends (JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = db.query(MovieModel).all()
    return JSONResponse(status_code =200, content=jsonable_encoder(result))

@movie_router.get("/movies/{id}", tags=['movies'], response_model = Movie)
def get_movie(id: int = Path(ge = 1, le = 2000)) -> Movie:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code = 404, content = {'message': 'No se encontró la pelicula'})
    return JSONResponse(status_code = 200, content = jsonable_encoder(result))

@movie_router.get("/movies/", tags=['movies'], response_model =  List[Movie])
def get_movies_by_category(category: str = Query(min_lenght = 5, max_length = 10)) -> List[Movie]:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.category == category).all()
    return JSONResponse(status_code = 200, content = jsonable_encoder(result))

@movie_router.post("/movies", tags=['movies'], response_model = dict, status_code = 201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    new_movie = MovieModel(**movie.dict())
    db.add(new_movie)
    db.commit()
    return JSONResponse(status_code = 201, content = {'message': 'Pelicula creada'})

@movie_router.put("/movies/{id}", tags=['movies'], response_model = dict)
def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code = 404, content = {'message': 'No se encontró la pelicula'}) 
    result.title = movie.title
    result.overview = movie.overview
    result.year = movie.year
    result.rating = movie.rating
    result.category = movie.category
    db.commit()
    return JSONResponse(status_code = 200, content = {'message': 'Pelicula actualizada'})

@movie_router.delete("/movies/{id}", tags=['movies'], response_model = dict)
def delete_movie(id: int) -> dict:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code = 404, content = {'message': 'No se encontró la pelicula'})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code = 200, content = {'message': 'Pelicula eliminada'})
```
En el archivo main.py

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from jwt_manager import create_token
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)

class User(BaseModel):
    email: str
    password: str

movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	},
    {
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]

@app.get("/", tags=['home'])
def message():
    return HTMLResponse('<h1>¡Hola mundo!</h1>')

@app.post("/login", tags=['auth'], response_model = dict)
def login(user: User) -> dict:
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(data = user.dict())
    return JSONResponse(status_code = 200, content = {'token': token})
```
## Servicios para consultar datos 
1. [Clase](https://platzi.com/clases/5355-fastapi-modularizacion-datos/57748-servicios-para-consultar-datos/)

en la carpeta services en el archivo movie.py

```python
from models.movie import Movie as MovieModel

class MovieService():

    def __init__(self, db) -> None:
        self.db = db
    
    def get_movies(self):
        result =  self.db.query(MovieModel).all()
        return result
    
    def get_movie(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result

```

en la carpeta router en el archivo movie.py
    
```python
@movie_router.get("/movies", tags=['movies'], response_model=List[Movie], status_code = 200, dependencies = [Depends (JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code =200, content=jsonable_encoder(result))

@movie_router.get("/movies/{id}", tags=['movies'], response_model = Movie)
def get_movie(id: int = Path(ge = 1, le = 2000)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code = 404, content = {'message': 'No se encontró la pelicula'})
    return JSONResponse(status_code = 200, content = jsonable_encoder(result))
```
## Servicios para registrar o modificar datos 

1. [Clase](https://platzi.com/clases/5355-fastapi-modularizacion-datos/57749-servicios-para-registrar-o-modificar-datos/)

Se crea la carpeta schemas y se guardan los esquemas de las clases 

```python
    def get_movies_by_category(self, category):
        result = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return result
    
    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return new_movie

    def update_movie(self, id: int, movie: Movie):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        result.title = movie.title
        result.overview = movie.overview
        result.year = movie.year
        result.rating = movie.rating
        result.category = movie.category
        self.db.commit()
        return result
```
# Despliegue
## Preparando el proyecto para desplegar a produccion 
1. [Clase](https://platzi.com/clases/5355-fastapi-modularizacion-datos/57750-preparando-el-proyecto-para-desplegar-a-produccion/)

## Creando el repositorio en GitLab
1. [Clase](https://platzi.com/clases/5355-fastapi-modularizacion-datos/57751-creando-el-repositorio-en-gitlab/)

## Creando el Droplet en DigitalOcean
1. [Clase](https://platzi.com/clases/5355-fastapi-modularizacion-datos/57752-creando-el-droplet-en-digitalocean/)

# Instalacion de herramientas para el servidor
1. [Clase](https://platzi.com/clases/5355-fastapi-modularizacion-datos/57753-instalacion-de-herramientas-para-el-servidor/)

# Ejecutando FastAPI con NGINX
1. [Clase](https://platzi.com/clases/5355-fastapi-modularizacion-datos/57754-ejecutando-fastapi-con-nginx/)
