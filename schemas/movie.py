from pydantic import BaseModel, Field
from typing import Optional

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