from typing import List

from pydantic import BaseModel


class Game(BaseModel):
    id:str
    ruleset: dict
    map: str
    timeout: int
    source: str


class Coord(BaseModel):
    x: int
    y: int

    def __eq__(self, other: "Coord") -> bool:
        return self.x == other.x and self.y == other.y


class Snake(BaseModel):
    id: str
    name: str
    health: int
    body: List[Coord]
    latency: str
    head: Coord
    length: int
    shout: str
    squad: str
    customizations: dict


class Board(BaseModel):
    width: int
    height: int
    food: List[Coord]
    hazards: List[Coord]
    snakes: List[Snake]
