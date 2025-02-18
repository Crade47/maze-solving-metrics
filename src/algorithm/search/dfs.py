
from collections import deque
from typing import Optional, Set, Tuple, List
from maze import Maze

CoordinateType = Tuple[int, int]

def reconstruct_path(
    came_from,
    start: CoordinateType,
    goal: CoordinateType,
) -> List[CoordinateType]:
    path = []
    current = goal
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path


class DFS:
    def __init__(self, maze: Maze):
        self.maze: Maze = maze

    def solve(self) -> List[CoordinateType]:
        start: CoordinateType = (0,0)
        goal: CoordinateType = (self.maze.height - 1, self.maze.width - 1)

        stack: List[CoordinateType] = [start]
        visited: Set[CoordinateType] = {start}
        came_from: dict[CoordinateType, Optional[CoordinateType]] = {start: None}


        while stack:
            r, c = stack.pop() 
            if (r,c) == goal:
                return reconstruct_path(came_from, start, goal)

            cell = self.maze.grid[r][c]

            for dr, dc, wall_key in [
                (-1, 0, "top"),    # up
                (1, 0, "bottom"),  # down
                (0, -1, "left"),   # left
                (0, 1, "right"),   # right
            ]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < self.maze.height and 0 <= nc < self.maze.width:
                    if not cell.walls[wall_key]:
                        neighbour = (nr, nc) 
                        if neighbour not in visited:
                            visited.add(neighbour)
                            stack.append(neighbour)
                            came_from[neighbour] = (r, c)
        return [] 






"""
FUNCTION DFS(maze, start_cell, goal_cell):
    CREATE an empty stack
    PUSH start_cell onto the stack
    CREATE a dictionary `came_from` to store the path
    MARK start_cell as visited

    WHILE stack is not empty:
        current_cell = POP from stack

        IF current_cell == goal_cell:
            RETURN RECONSTRUCT_PATH(came_from, start_cell, goal_cell)  // Path found

        FOR each possible direction (UP, DOWN, LEFT, RIGHT):
            next_cell = cell in that direction
            IF next_cell is within maze bounds AND next_cell is not visited AND no wall blocks the path:
                PUSH next_cell onto stack
                MARK next_cell as visited
                STORE `came_from[next_cell] = current_cell`  // Track path

    RETURN None  // No path found
"""


