from jose import JWTError
from lilya._internal._connection import Connection
from lilya.types import ASGIApp

from esmerald.config.jwt import JWTConfig
from esmerald.conf import settings
from esmerald.exceptions import NotAuthorized
from esmerald.middleware.authentication import AuthResult, BaseAuthMiddleware
from esmerald.security.jwt.token import Token
from esmerald.utils.module_loading import import_string

from edgy.exceptions import ObjectNotFound

from .anonymous_user import NotAuthResult

User = import_string("src.models.User")


class JWTAuthMiddleware(BaseAuthMiddleware):
    # def __init__(self, app: "ASGIApp", config: "JWTConfig"):
    #     super().__init__(app)
    #     self.app = app
    #     self.config = config

    async def retrieve_user(self, user_id: int) -> User:
        try:
            return await User.query.get(pk=user_id)
        except ObjectNotFound:
            raise NotAuthorized()

    async def authenticate(self, request: Connection) -> AuthResult | NotAuthResult:
        auth_header = request.headers.get(settings.simple_jwt.authorization_header)

        if not auth_header:
            raise NotAuthorized(detail="Authorization header not found.")

        auth_header = auth_header.split()

        if auth_header[0].lower() != 'bearer':
            raise NotAuthorized(detail="Invalid token.")

        if len(auth_header) == 1:
            raise NotAuthorized(detail="Invalid token header. No credential provided.")
        elif len(auth_header) > 2:
            raise NotAuthorized(
                detail="Invalid token header. Token string should not contain spaces"
            )

        try:
            token = Token.decode(
                token=auth_header[1],
                key=settings.simple_jwt.signing_key,
                algorithms=settings.simple_jwt.algorithm
            )
        except JWTError:
            raise NotAuthorized(detail="Invalid authentication. Could not decode token.")

        user = await self.retrieve_user(int(token.sub))
        return AuthResult(user=user)
