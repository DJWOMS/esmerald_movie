from src.apps.category.dtos import CreateCategoryDTO, CategoryDTO, UpdateCategoryDTO
from src.apps.category.repository import CategoryRepository
from src.models import Category


class CategoryService:

    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    async def create(self, dto: CreateCategoryDTO) -> Category:
        return await self.repository.create(dto)

    async def update(self, pk: int, dto: UpdateCategoryDTO) -> Category:
        return await self.repository.update(pk, dto)

    async def delete(self, pk: int) -> Category:
        return await self.repository.delete(pk)

    async def get_by_id(self, pk: int) -> Category:
        return await self.repository.get(pk=pk)

    async def get_list(self) -> list[CategoryDTO]:
        return await self.repository.get_all()
