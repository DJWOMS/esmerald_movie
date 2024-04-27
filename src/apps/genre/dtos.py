from pydantic import BaseModel


class GenreBaseDTO(BaseModel):
    name: str
    description: str
    url: str


class CreateGenreDTO(GenreBaseDTO):
    pass


class UpdateGenreDTO(GenreBaseDTO):
    pass


class GenreDTO(GenreBaseDTO):
    id: int
