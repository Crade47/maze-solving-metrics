
from typing import List, Tuple


def reconstruct_path(
    came_from,
    start: Tuple[int, int],
    goal: Tuple[int, int],
) -> List[Tuple[int, int]]:
    path = []
    current = goal
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path


