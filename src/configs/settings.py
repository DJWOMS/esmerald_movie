from functools import cached_property
from typing import Optional
from pydantic import Field

from edgy import Database, Registry
from esmerald.conf.enums import EnvironmentType
from esmerald.conf.global_settings import EsmeraldAPISettings

from esmerald_simple_jwt.config import SimpleJWT


class AppSettings(EsmeraldAPISettings):
    app_name: str = "My application in production mode."
    title: str = "My src"
    environment: Optional[str] = EnvironmentType.PRODUCTION
    secret_key: str = "esmerald-insecure-0qoii(%&amp;zrx!l+y$43=v6%)3m%hp-%hm2gqo@o312)80y4q2eo"
    user: str = Field(..., alias="POSTGRES_USER")
    password: str = Field(..., alias="POSTGRES_PASSWORD")
    host: str = Field(..., alias="POSTGRES_HOST")
    port: str = Field(..., alias="POSTGRES_PORT")
    url_schema: str = Field("postgresql+asyncpg", alias="DB_URL_SCHEME")
    name: str = Field(..., alias="POSTGRES_DB")

    @cached_property
    def registry(self) -> tuple[Database, Registry]:
        database = Database(self.url)
        return database, Registry(database=database)

    @property
    def url(self) -> str:
        return f"{self.url_schema}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

    @property
    def simple_jwt(self) -> SimpleJWT:
        from src.apps.account.backends import BackendAuthentication, RefreshAuthentication

        return SimpleJWT(
            signing_key=self.secret_key,
            backend_authentication=BackendAuthentication,
            backend_refresh=RefreshAuthentication,
        )

