from collections import deque
from typing import Optional, Tuple, List, Dict
from maze import Maze
from utils.utils import reconstruct_path
from utils import Heuristic
import heapq

CoordinateType = Tuple[int, int]


class AStar:
    def __init__(self, maze: Maze):
        self.maze = maze
        self.heuristic = Heuristic()

    def solve(self) -> List[CoordinateType]:
        start: CoordinateType = (0, 0)
        goal: CoordinateType = (self.maze.height - 1, self.maze.width - 1)

        open_set: List[Tuple[float, CoordinateType]] = []
        heapq.heappush(open_set, (0, start))  # (f, node)

        # To reconstruct the path
        came_from: Dict[CoordinateType, Optional[CoordinateType]] = {start: None}

        # Cost from start to each node
        g_score: Dict[CoordinateType, float] = {start: 0}

        # Heuristic estimates from node to goal
        f_score: Dict[CoordinateType, float] = {start: self.heuristic.manhattan_heuristic(start, goal)}

        # Set of nodes already evaluated
        closed_set: set[CoordinateType] = set()

        while open_set:
            # Get the node in the open set with the lowest f_score
            _, current = heapq.heappop(open_set)
            
            if current == goal:
                return reconstruct_path(came_from, start, goal)

            closed_set.add(current)

            r, c = current
            cell = self.maze.grid[r][c]
            
            for dr, dc, wall_key in [
                (-1, 0, "top"),    # up
                (1, 0, "bottom"),  # down
                (0, -1, "left"),   # left
                (0, 1, "right"),   # right
            ]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.maze.height and 0 <= nc < self.maze.width:
                    if not cell.walls.get(wall_key, True) and (nr, nc) not in closed_set:
                        tentative_g_score = g_score[current] + 1  # Assume uniform cost of 1 for each move
                        
                        if (nr, nc) not in g_score or tentative_g_score < g_score[(nr, nc)]:
                            came_from[(nr, nc)] = current
                            g_score[(nr, nc)] = tentative_g_score
                            f_score[(nr, nc)] = g_score[(nr, nc)] + self.heuristic.manhattan_heuristic((nr, nc), goal)
                            heapq.heappush(open_set, (f_score[(nr, nc)], (nr, nc)))


        return []
