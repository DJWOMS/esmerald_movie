from pydantic import BaseModel


class NotAuthResult(BaseModel):
    user: None = None
