from src.apps.actor.dtos import CreateActorDTO, ActorDTO, UpdateActorDTO
from src.apps.actor.repository import ActorRepository
from src.models import Actor


class ActorService:

    def __init__(self, repository: ActorRepository):
        self.repository = repository

    async def create(self, dto: CreateActorDTO) -> Actor:
        return await self.repository.create(dto)

    async def update(self, pk: int, dto: UpdateActorDTO) -> Actor:
        return await self.repository.update(pk, dto)

    async def delete(self, pk: int) -> Actor:
        return await self.repository.delete(pk)

    async def get_by_id(self, pk: int) -> Actor:
        return await self.repository.get(pk=pk)

    async def get_list(self) -> list[ActorDTO]:
        return await self.repository.get_all()
