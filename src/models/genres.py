import edgy

from .base import BaseModel


class Genre(BaseModel):
    """Жанры"""
    name: str = edgy.CharField(max_length=100)
    description: str = edgy.TextField()
    url: str = edgy.URLField(max_length=160, unique=True)
