from .cell import Cell
import random


class Maze:
    def __init__(self, size: int) -> None:
        self.width: int = size
        self.height: int = size

        # Create grid with (row, column) coordinates.
        self.grid = [
            [Cell(r, c) for c in range(self.width)] for r in range(self.height)
        ]
        # Each cell's parent is keyed by (row, col)
        self.parent = {
            (r, c): (r, c) for r in range(self.height) for c in range(self.width)
        }

    def find(self, cell_coord):
        if self.parent[cell_coord] != cell_coord:
            self.parent[cell_coord] = self.find(self.parent[cell_coord])
        return self.parent[cell_coord]

    def union(self, cell_coord1, cell_coord2):
        root1 = self.find(cell_coord1)
        root2 = self.find(cell_coord2)
        if root1 != root2:
            self.parent[root2] = root1

    def generate(self):
        # Build list of potential walls between adjacent cells.
        # Each wall: ((row, col), (neighbor_row, neighbor_col), wall_in_cell, wall_in_neighbor)
        walls = []
        for r in range(self.height):
            for c in range(self.width):
                # Right neighbor: (r, c) → (r, c+1)
                if c < self.width - 1:
                    walls.append(((r, c), (r, c + 1), "right", "left"))
                # Bottom neighbor: (r, c) → (r+1, c)
                if r < self.height - 1:
                    walls.append(((r, c), (r + 1, c), "bottom", "top"))

        random.shuffle(walls)

        for cell_coord1, cell_coord2, wall1, wall2 in walls:
            if self.find(cell_coord1) != self.find(cell_coord2):
                cell1 = self.grid[cell_coord1[0]][cell_coord1[1]]
                cell2 = self.grid[cell_coord2[0]][cell_coord2[1]]
                cell1.walls[wall1] = False
                cell2.walls[wall2] = False
                self.union(cell_coord1, cell_coord2)

        return self.grid

    def display(self):
        # Simple text-based maze visualization.
        # Top border
        maze_rows = []
        top_line = " " + "_" * (self.width * 2 - 1)
        maze_rows.append(top_line)
        for y in range(self.height):
            row = "|"
            for x in range(self.width):
                cell = self.grid[y][x]
                # If the bottom wall is present, use '_' otherwise a space.
                if cell.walls["bottom"]:
                    floor = "_"
                else:
                    floor = " "
                # If the right wall is present, use '|' otherwise a space.
                if cell.walls["right"]:
                    wall = "|"
                else:
                    wall = " "
                row += floor + wall
            maze_rows.append(row)
        # Print the maze rows
        for row in maze_rows:
            print(row)
