# from __future__ import annotations

from typing import TYPE_CHECKING

from esmerald import APIView, delete, get, post, put, status, Inject, File, Form, UploadFile, JSONResponse
from esmerald.openapi.security.http import Bearer

from src.apps.account.permissions import IsUserAdmin

from src.models import Actor

from src.apps.actor.dtos import CreateActorDTO, ActorDTO, UpdateActorDTO
from src.apps.actor.repository import ActorRepository
from src.apps.actor.service import ActorService

if TYPE_CHECKING:
    from esmerald.types import Dependencies


class ActorAPIView(APIView):
    # path: str = "/actors"
    security = [Bearer]
    permissions = [IsUserAdmin]
    tags = ["Actor"]
    dependencies = {
        "repository": Inject(ActorRepository),
        "service": Inject(ActorService),
    }

    @post("/")
    async def create(self, service: ActorService, data: CreateActorDTO = Form()) -> Actor:
        content = await data.read()
        name = data.filename
        return JSONResponse({"filename": name, "content": content.decode()})
        # return await service.create(data)

    @get("/{pk:int}")
    async def get_by_id(self, pk: int, service: ActorService) -> Actor:
        return await service.get_by_id(pk)

    @get("/", summary="Get all actors")
    async def get_all(self, service: ActorService) -> list[ActorDTO]:
        return await service.get_list()

    @put("/{pk:int}")
    async def update(self, pk: int, data: UpdateActorDTO, service: ActorService) -> Actor:
        return await service.update(pk, data)

    @delete("/{pk:int}", status_code=status.HTTP_200_OK)
    async def delete(self, pk: int, service: ActorService) -> None:
        return await service.delete(pk)
