from collections import deque
from typing import Dict, List, Optional, Tuple

from maze.cell import Cell
from maze.maze import Maze


def reconstruct_path(
    came_from,
    start: tuple[int, int],
    goal: tuple[int, int],
) -> List[tuple]:
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

    def solve(self) -> Optional[List[Tuple]]:
        start = (0, 0)
        goal = (self.maze.height - 1, self.maze.width - 1)

        frontier = deque([start])
        came_from: dict[tuple[int,int], Optional[tuple[int, int]]] = {start: None}

        while frontier:
            x, y = frontier.popleft()
            if (x, y) == goal:
                return reconstruct_path(came_from, start, goal)
            cell = self.maze.grid[y][x]
            for dx, dy, wall_key in [
                (1, 0, "right"),  # right neighbor
                (-1, 0, "left"),  # left neighbor
                (0, 1, "bottom"),  # bottom neighbor
                (0, -1, "top"),  # top neighbor
            ]:
                nx, ny = x + dx, x + dy
                #checking if the neighbor is within bounds
                if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height:
                    if not cell.walls[wall_key]:
                        if (nx, ny) not in came_from:
                            came_from[(nx, ny)] = (x, y)
        return None 


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
