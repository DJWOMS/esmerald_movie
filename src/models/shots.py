import edgy

from . import Movie
from .base import BaseModel


class MovieShots(BaseModel):
    """Кадры из фильма"""
    title: str = edgy.CharField(max_length=100)
    description: str = edgy.TextField()
    image: str = edgy.CharField(max_length=500)
    movie: Movie = edgy.ForeignKey(Movie, on_delete=edgy.CASCADE)
