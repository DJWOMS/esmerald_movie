from src.apps.genre.dtos import CreateGenreDTO, UpdateGenreDTO, GenreDTO
from src.apps.genre.repository import GenreRepository
from src.models import Genre


class GenreService:

    def __init__(self, repository: GenreRepository):
        self.repository = repository

    async def create(self, dto: CreateGenreDTO) -> Genre:
        return await self.repository.create(dto)

    async def update(self, pk: int, dto: UpdateGenreDTO) -> Genre:
        return await self.repository.update(pk, dto)

    async def delete(self, pk: int) -> Genre:
        return await self.repository.delete(pk)

    async def get_by_id(self, pk: int) -> Genre:
        return await self.repository.get(pk=pk)

    async def get_list(self) -> list[Genre]:
        return await self.repository.get_all()
