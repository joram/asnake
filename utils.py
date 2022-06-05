from typing import List, Optional

from enums import Directions
from models import Coord


def distance(a: Coord, b: Coord) -> int:
    x_delta = abs(a.x - b.x)
    y_delta = abs(a.y - b.y)
    return x_delta + y_delta


def closest(start: Coord, targets: List[Coord]) -> Optional[Coord]:
    best_dist = None
    best_coord = None
    for coord in targets:
        dist = distance(start, coord)
        if best_dist is None or dist < best_dist:
            best_coord = coord
            best_dist = dist
    return best_coord


def direction(start: Coord, end: Coord) -> Directions:
    if start.x < end.x:
        return Directions.RIGHT

    if start.x > end.x:
        return Directions.LEFT

    if start.y > end.y:
        return Directions.DOWN

    return Directions.UP
