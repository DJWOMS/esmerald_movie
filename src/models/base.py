from datetime import datetime

import edgy

from esmerald.conf import settings


database, models = settings.registry


class BaseModel(edgy.Model):
    id: int = edgy.IntegerField(primary_key=True)
    created_at: datetime = edgy.DateTimeField(auto_now_add=True)
    updated_at: datetime = edgy.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        registry = models

    def to_dict(self):
        return self.model_dump()
