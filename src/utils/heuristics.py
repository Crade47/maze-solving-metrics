from typing import Tuple

from utils.types import CoordinateType




class Heuristic:

    def __init__(self) -> None:
        pass

    def manhattan_heuristic(self, a: CoordinateType, b: CoordinateType) -> float:
        """
        Heuristic function for A*.
        Using Manhattan distance as the heuristic (grid-based search).
        params:
        a, b: coordinates of the maze
        """
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
