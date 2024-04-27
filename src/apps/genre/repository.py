from src.apps.genre.dtos import CreateGenreDTO, UpdateGenreDTO

from src.models import Genre


class GenreRepository:
    model = Genre

    async def create(self, dto: CreateGenreDTO) -> Genre:
        return await self.model.query.create(**dto.model_dump())

    async def get(self, pk: int) -> Genre | None:
        return await self.model.query.get_or_none(id=pk)

    async def get_by_name(self, name: str) -> Genre:
        return await self.model.query.get(name=name)

    async def get_all(self) -> list[Genre]:
        return await self.model.query.all()

    async def update(self, pk: int, dto: UpdateGenreDTO):
        return await self.model.query.filter(id=pk).update(**dto.model_dump())

    async def delete(self, pk: int):
        return await self.model.query.filter(id=pk).delete()
