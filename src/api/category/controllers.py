# from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Any

from esmerald import APIView, delete, get, post, put, status, Inject, Factory
from esmerald.openapi.security.http import Bearer

from src.apps.account.permissions import IsUserAdmin

from src.apps.category.dtos import CreateCategoryDTO, CategoryDTO, UpdateCategoryDTO
from src.apps.category.repository import CategoryRepository
from src.models import Category
from src.apps.category.service import CategoryService

if TYPE_CHECKING:
    from esmerald.types import Dependencies


class CategoryAPIView(APIView):
    # path: str = "/category"
    security = [Bearer]
    permissions = [IsUserAdmin]
    tags = ["Category"]
    dependencies = {
        "repository": Inject(CategoryRepository),
        "service": Inject(CategoryService),
    }

    @post("/")
    async def create(self, data: CreateCategoryDTO, service: CategoryService) -> Category:
        return await service.create(data)

    @get("/{pk:int}")
    async def get_by_id(self, pk: int, service: CategoryService) -> Category:
        return await service.get_by_id(pk)

    @get("/", summary="Get all categories")
    async def get_all(self, service: CategoryService) -> list[CategoryDTO]:
        return await service.get_list()

    @put("/{pk:int}")
    async def update(self, pk: int, data: UpdateCategoryDTO, service: CategoryService) -> Category:
        return await service.update(pk, data)

    @delete("/{pk:int}", status_code=status.HTTP_200_OK)
    async def delete(self, pk: int, service: CategoryService) -> None:
        return await service.delete(pk)
