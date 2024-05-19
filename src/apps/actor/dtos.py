from pydantic import BaseModel
from esmerald import File, UploadFile


class ActorBaseDTO(BaseModel):
    name: str
    age: int
    description: str
    image: UploadFile = File()


class CreateActorDTO(ActorBaseDTO):
    pass


class UpdateActorDTO(ActorBaseDTO):
    pass


class ActorDTO(ActorBaseDTO):
    id: int
