from esmerald.contrib.auth.edgy.base_user import AbstractUser

from .base import BaseModel


class User(AbstractUser, BaseModel):
    pass

