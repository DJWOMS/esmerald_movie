from src.apps.category.dtos import CreateCategoryDTO, UpdateCategoryDTO, CategoryDTO

from src.models import Category


class CategoryRepository:
    model = Category

    async def create(self, dto: CreateCategoryDTO):
        return await self.model.query.create(**dto.model_dump())

    async def get(self, pk: int) -> CategoryDTO | None:
        return await self.model.query.get_or_none(id=pk)

    async def get_by_name(self, name: str) -> CategoryDTO:
        return await self.model.query.get(name=name)

    async def get_all(self):
        return await self.model.query.all()

    async def update(self, pk: int, dto: UpdateCategoryDTO):
        return await self.model.query.filter(id=pk).update(**dto.model_dump())

    async def delete(self, pk: int):
        return await self.model.query.filter(id=pk).delete()
