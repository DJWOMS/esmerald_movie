import edgy

from . import Movie
from .base import BaseModel


class Review(BaseModel):
    """Отзывы"""
    email: str = edgy.EmailField(max_length=250)
    name: str = edgy.CharField(max_length=100)
    text: str = edgy.TextField(max_length=5000)
    parent = edgy.ForeignKey('Review', on_delete=edgy.SET_NULL, null=True, related_name="children")
    movie: Movie = edgy.ForeignKey(Movie, on_delete=edgy.CASCADE, related_name="reviews")
