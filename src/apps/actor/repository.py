from src.apps.actor.dtos import CreateActorDTO, UpdateActorDTO, ActorDTO

from src.models import Actor


class ActorRepository:
    model = Actor

    async def create(self, dto: CreateActorDTO) -> Actor:
        return await self.model.query.create(**dto.model_dump())

    async def get(self, pk: int) -> Actor | None:
        return await self.model.query.get_or_none(id=pk)

    async def get_by_name(self, name: str) -> Actor:
        return await self.model.query.get(name=name)

    async def get_all(self):
        return await self.model.query.all()

    async def update(self, pk: int, dto: UpdateActorDTO):
        return await self.model.query.filter(id=pk).update(**dto.model_dump())

    async def delete(self, pk: int):
        return await self.model.query.filter(id=pk).delete()
