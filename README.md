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

