import edgy

from .base import BaseModel


class Actor(BaseModel):
    """Актеры и режиссеры"""
    name: str = edgy.CharField(max_length=100)
    age: int = edgy.IntegerField(default=0)
    description: str = edgy.TextField()
    image: str = edgy.CharField(max_length=500)
