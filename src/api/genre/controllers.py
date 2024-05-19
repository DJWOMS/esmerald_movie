# from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from esmerald import APIView, delete, get, post, put, status, Inject
from esmerald.openapi.security.http import Bearer

from src.apps.account.permissions import IsUserAdmin
from src.models import Genre

from src.apps.genre.repository import GenreRepository
from src.apps.genre.service import GenreService
from src.apps.genre.dtos import CreateGenreDTO, UpdateGenreDTO


if TYPE_CHECKING:
    from esmerald.types import Dependencies


T = TypeVar("T")


class GenreAPIView(APIView):
    # path: str = "/genre"
    security = [Bearer]
    permissions = [IsUserAdmin]
    tags: list["str"] = ["Genre"]
    dependencies: "Dependencies" = {
        "repository": Inject(GenreRepository),
        "service": Inject(GenreService),
    }

    @post("/")
    async def create(self, data: CreateGenreDTO, service: GenreService) -> Genre:
        return await service.create(data)

    @get("/{pk:int}")
    async def get_by_id(self, pk: int, service: GenreService) -> Genre:
        return await service.get_by_id(pk)

    @get("/", summary="Get all categories")
    async def get_all(self, service: GenreService) -> list[Genre]:
        return await service.get_list()

    @put("/{pk:int}")
    async def update(self, pk: int, data: UpdateGenreDTO, service: GenreService) -> Genre:
        return await service.update(pk, data)

    @delete("/{pk:int}", status_code=status.HTTP_200_OK)
    async def delete(self, pk: int, service: GenreService) -> None:
        return await service.delete(pk)
