from pydantic import BaseModel


class CategoryBaseDTO(BaseModel):
    name: str
    description: str
    url: str


class CreateCategoryDTO(CategoryBaseDTO):
    pass


class UpdateCategoryDTO(CategoryBaseDTO):
    pass


class CategoryDTO(CategoryBaseDTO):
    id: int
