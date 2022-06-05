from typing import Optional

from pydantic import BaseModel

from enums import Directions


class RootResponse(BaseModel):
    apiversion: str = "1"
    author: str = "MyUsername"
    color: str = "#888888"
    head: str = "default"
    tail: str = "default"
    version: str = "1.0"


class MoveResponse(BaseModel):
    move: Directions = Directions.UP
    shout: Optional[str] = None
