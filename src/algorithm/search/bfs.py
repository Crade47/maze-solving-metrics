from collections import deque
from typing import Dict, List, Optional, Tuple

from maze import Maze
from utils.utils import reconstruct_path

class BFS:
    def __init__(self, maze: Maze):
        self.maze = maze

    def solve(self) -> Optional[List[Tuple[int, int]]]:
        start = (0, 0)  # (row, column)
        goal = (self.maze.height - 1, self.maze.width - 1)

        frontier: deque[Tuple[int, int]] = deque([start])
        came_from: dict[Tuple[int, int], Optional[Tuple[int, int]]] = {start: None}

        while frontier:
            r, c = frontier.popleft()
            if (r, c) == goal:
                return reconstruct_path(came_from, start, goal)
            
            cell = self.maze.grid[r][c]
            # Neighbors: (dr, dc) offsets with corresponding wall keys
            for dr, dc, wall_key in [
                (-1, 0, "top"),    # up
                (1, 0, "bottom"),  # down
                (0, -1, "left"),   # left
                (0, 1, "right"),   # right
            ]:
                nr, nc = r + dr, c + dc
                # Check bounds
                if 0 <= nr < self.maze.height and 0 <= nc < self.maze.width:
                    # Check that there is no wall in the current cell in the direction we're moving
                    if not cell.walls[wall_key]:
                        if (nr, nc) not in came_from:
                            came_from[(nr, nc)] = (r, c)
                            frontier.append((nr, nc))
        return [] 

