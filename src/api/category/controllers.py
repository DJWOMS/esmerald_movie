from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Any

from esmerald import APIView, delete, get, post, put, status, Inject, Factory

from src.apps.category.dtos import CreateCategoryDTO, CategoryDTO
from src.apps.category.repository import CategoryRepository
from src.models import Category
from src.apps.category.service import CategoryService

if TYPE_CHECKING:
    from esmerald.types import Dependencies



T = TypeVar("T")


class CategoryAPIView(APIView):
    # path: str = "/category"
    tags = ["Category"]
    dependencies = {
        "repository": Inject(CategoryRepository),
        "service": Inject(CategoryService),
    }

    # @post("/")
    # async def create(self, data: CreateCategoryDTO, service: CategoryService) -> CategoryDTO:
    #     return await service.create(data)

    # @get("/{pk:int}")
    # async def get_by_id(self, pk: int, service: "CategoryService") -> Category:
    #     return await service.get_by_id(pk)
    #
    @get("/", summary="Get all categories")
    async def get_all(self, service: "CategoryService") -> list[CategoryDTO]:
        return await service.get_list()

    # @put("/{pk:int}")
    # async def update(self, pk: int) -> T: ...
    #
    # @delete("/{pk:int}")
    # async def delete_by_id(self, pk: int) -> T: ...
