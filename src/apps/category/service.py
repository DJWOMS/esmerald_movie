from src.apps.category.dtos import CreateCategoryDTO, CategoryDTO
from src.apps.category.repository import CategoryRepository


class CategoryService:

    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    # async def create(self, dto: CreateCategoryDTO) -> Category:
    #     return await self.model.query.create(**dto.model_dump())

    async def update(self):
        pass

    async def delete(self):
        pass

    # async def get_by_id(self, pk: int) -> Category:
    #     return await self.model.query.get(id=pk)

    async def get_list(self) -> list[CategoryDTO]:
        return await self.repository.get_all()
