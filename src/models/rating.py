import edgy

from . import Movie
from .base import BaseModel


class RatingStar(BaseModel):
    """Звезда рейтинга"""
    value: int = edgy.SmallIntegerField(default=0)


class Rating(BaseModel):
    """Рейтинг"""
    ip: str = edgy.CharField(max_length=15)
    star: RatingStar = edgy.ForeignKey(RatingStar, on_delete=edgy.CASCADE)
    movie: Movie = edgy.ForeignKey(Movie, on_delete=edgy.CASCADE, related_name="ratings")
