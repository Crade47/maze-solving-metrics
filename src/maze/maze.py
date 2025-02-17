from .cell import Cell
import random
class Maze:
    def __init__(self, size) -> None:
        self.width = size
        self.height = size
        self.size = size
        self.grid = [[Cell(x, y) for x in range(self.width)] for y in range(self.height)]
        # Initialize union-find parent dictionary; each cell is its own parent initially.
        self.parent = {(x, y): (x, y) for y in range(self.height) for x in range(self.width)}
    
    def find(self, cell_coord):
        # Path compression for union-find
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
        # Each wall is represented as a tuple:
        # ((x1, y1), (x2, y2), wall_in_cell1, wall_in_cell2)
        walls = []
        for y in range(self.height):
            for x in range(self.width):
                # Right neighbor
                if x < self.width - 1:
                    walls.append(((x, y), (x + 1, y), 'right', 'left'))
                # Bottom neighbor
                if y < self.height - 1:
                    walls.append(((x, y), (x, y + 1), 'bottom', 'top'))
        
        # Randomize the order of walls
        random.shuffle(walls)
        
        # Process each wall in random order
        for cell_coord1, cell_coord2, wall1, wall2 in walls:
            if self.find(cell_coord1) != self.find(cell_coord2):
                # Remove the wall between the two cells
                cell1 = self.grid[cell_coord1[1]][cell_coord1[0]]
                cell2 = self.grid[cell_coord2[1]][cell_coord2[0]]
                cell1.walls[wall1] = False
                cell2.walls[wall2] = False
                # Merge the sets
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
                if cell.walls['bottom']:
                    floor = "_"
                else:
                    floor = " "
                # If the right wall is present, use '|' otherwise a space.
                if cell.walls['right']:
                    wall = "|"
                else:
                    wall = " "
                row += floor + wall
            maze_rows.append(row)
        # Print the maze rows
        for row in maze_rows:
            print(row)

