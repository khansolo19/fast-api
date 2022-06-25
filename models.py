from datetime import datetime
from typing import Optional
import ormar

from db import metadata,database


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database =database


class User(ormar.Model):
    class Meta(MainMeta):
        pass
    
    id: int = ormar.Integer(primary_key=True)
    username: str =  ormar.String(max_length=100)


class Video(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=255)
    description: str = ormar.String(max_length=1000)
    file: str = ormar.String(max_length=1000)
    created_at: datetime = ormar.DateTime(default=datetime.now())
    owner: Optional[User] = ormar.ForeignKey(User)