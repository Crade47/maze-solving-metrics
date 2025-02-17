import matplotlib.pyplot as plt
import numpy as np

class Visualizer:

    def __init__(self, maze) -> None:
        self.maze = maze  # maze is a grid (list of lists) of Cell objects
        self.height = len(maze)
        self.width = len(maze[0]) if self.height > 0 else 0

    def visualize(self):
        # Create a grid for visualization:
        # Size: (2*height + 1) x (2*width + 1)
        # Initialize with ones (walls)
        grid = np.ones((self.height * 2 + 1, self.width * 2 + 1), dtype=int)

        # Set cell centers as passages
        for y in range(self.height):
            for x in range(self.width):
                grid[y * 2 + 1, x * 2 + 1] = 0  # cell center

                cell = self.maze[y][x]

                # If no top wall, remove wall above cell center
                if not cell.walls['top']:
                    grid[y * 2, x * 2 + 1] = 0
                # If no bottom wall, remove wall below cell center
                if not cell.walls['bottom']:
                    grid[y * 2 + 2, x * 2 + 1] = 0
                # If no left wall, remove wall to the left of cell center
                if not cell.walls['left']:
                    grid[y * 2 + 1, x * 2] = 0
                # If no right wall, remove wall to the right of cell center
                if not cell.walls['right']:
                    grid[y * 2 + 1, x * 2 + 2] = 0

        # Plot using pcolormesh
        plt.figure(figsize=(10, 10))
        plt.pcolormesh(grid, cmap='binary', edgecolors='k', linewidth=0.5)
        plt.gca().set_aspect('equal')
        plt.axis('off')
        plt.show()
