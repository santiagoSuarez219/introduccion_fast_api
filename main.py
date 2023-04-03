from fastapi import FastAPI, Body, Path, Query, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from tiping import Optional, List
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Invalid token")

class User(BaseModel):
    email: str
    password: str

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

@app.get("/movies", tags=['movies'], response_model=List[Movie], status_code = 200, dependencies = [Depends (JWTBearer())])
def get_movies() -> List[Movie]:
    return JSONResponse(status_code =200, content=movies)

@app.get("/movies/{id}", tags=['movies'], response_model = Movie)
def get_movie(id: int = Path(ge = 1, le = 2000)) -> Movie:
    for item in movies:
        if item['id'] == id:
            return JSONResponse(content = item)
    return JSONResponse(status_code = 404, content = {'message': 'No se encontró la pelicula'})

@app.get("/movies/", tags=['movies'], response_model =  List[Movie])
def get_movies_by_category(category: str = Query(min_lenght = 5, max_length = 10)) -> List[Movie]:
    data = [item for item in movies if item['category'] == category]
    return JSONResponse(content = data)

@app.post("/movies", tags=['movies'], response_model = dict, status_code = 201)
def create_movie(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(status_code = 201, content = {'message': 'Pelicula creada'})

@app.put("/movies/{id}", tags=['movies'], response_model = dict)
def update_movie(id: int, movie: Movie) -> dict:
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            return JSONResponse(content = {'message': 'Pelicula actualizada'})

@app.delete("/movies/{id}", tags=['movies'], response_model = dict)
def delete_movie(id: int) -> dict:
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return JSONResponse(content = {'message': 'Pelicula eliminada'})