from esmerald import Request
from esmerald.permissions.base import BaseAbstractUserPermission
from esmerald.types import APIGateHandler


class IsUserAdmin(BaseAbstractUserPermission):
    """
    Simply check if a user has admin access or not.

    BaseAbstractUserPermission inherits from BasePermission.
    """

    def is_user_authenticated(self, request: "Request") -> bool:
        """
        Logic to check if the user is authenticated
        """
        ...

    def is_user_staff(self, request: "Request") -> bool:
        """
        Logic to check if user is staff
        """
        return bool(request.user and request.user.is_superuser)

    async def has_permission(self, request: "Request", apiview: "APIGateHandler"):
        super().has_permission(request, apiview)
        return bool(request.user and self.is_user_staff(request))

