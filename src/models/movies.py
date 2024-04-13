from typing import TYPE_CHECKING


from datetime import date

import edgy

from .actors import Actor
from .base import BaseModel
from .categories import Category
from .genres import Genre

# if TYPE_CHECKING:


class Movie(BaseModel):
    """Фильм"""
    title: str = edgy.CharField(max_length=100)
    tagline: str = edgy.CharField(max_length=100, default='')
    description: str = edgy.TextField()
    poster: str = edgy.CharField(max_length=500)
    year: int = edgy.IntegerField(default=2019)
    country: str = edgy.CharField(max_length=30)
    world_premiere: date = edgy.DateField()
    budget: int = edgy.IntegerField(default=0)
    fees_in_usa: int = edgy.IntegerField(default=0)
    fess_in_world: int = edgy.IntegerField(default=0)
    url: str = edgy.URLField(max_length=130, unique=True)
    draft: bool = edgy.BooleanField(default=False)
    directors: list["Actor"] = edgy.ManyToMany(Actor, related_name="film_director")
    actors: list["Actor"] = edgy.ManyToManyField(Actor, related_name="film_actor")
    genres: list["Genre"] = edgy.ManyToManyField(Genre)
    category: "Category" = edgy.ForeignKey("Category", on_delete=edgy.SET_NULL, null=True)

