import edgy

from .base import BaseModel


class Category(BaseModel):
    """Категории"""
    name: str = edgy.CharField(max_length=150)
    description: str = edgy.TextField()
    url: str = edgy.URLField(max_length=160, unique=True)

    class Meta:
        tablename = "categories"
