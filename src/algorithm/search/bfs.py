from collections import deque
from typing import Dict, List, Optional, Tuple

from maze import Maze


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

"""
    def bfs_solve(self):
        start = (0, 0)
        goal = (self.maze.width - 1, self.maze.height - 1)

        queue = deque([start])           # Our frontier of cells to explore
        came_from = {start: None}        # To track the path back to the start

        while queue:
            x, y = queue.popleft()       # Dequeue the current cell

            # Check if we reached the goal:
            if (x, y) == goal:
                return reconstruct_path(came_from, start, goal)

            cell = self.maze.grid[y][x]       # Get the current cell from the grid

            # Explore the four possible directions:
            for dx, dy, wall_key, opposite_wall in [
                (1, 0, "right", "left"),
                (-1, 0, "left", "right"),
                (0, 1, "bottom", "top"),
                (0, -1, "top", "bottom")
            ]:
                nx, ny = x + dx, y + dy

                # Check bounds:
                if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height:
                    # Check if the current cell has an open passage in the direction we're looking:
                    if not cell.walls[wall_key]:
                        if (nx, ny) not in came_from:  # Not visited yet
                            queue.append((nx, ny))
                            came_from[(nx, ny)] = (x, y)
        return None  # Should not happen for a perfect self.maze
"""
