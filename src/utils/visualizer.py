from typing import Optional, List, Tuple
import matplotlib.pyplot as plt
from maze import Maze

class Visualizer:
    def __init__(self, maze: Maze) -> None:
        """
        Initialize the visualizer with a maze.
        The maze should have:
          - maze.height and maze.width for dimensions.
          - maze.grid as a 2D list of cells, where each cell has a 'walls' dict.
            The walls dict should have keys: 'top', 'right', 'bottom', 'left'
            with a Boolean indicating whether the wall is closed (True) or open (False).
          - This is basically an instance of the Maze class in maze/maze.py
        """
        self.maze: Maze = maze

    def visualize(self, path: Optional[List[Tuple[int, int]]] = None) -> None:
        """
        Draws the maze using matplotlib.
        
        Parameters:
            path (optional): A list of (row, col) tuples representing the solution
                             path. If provided, the path is drawn in red.
        """
        _, ax = plt.subplots(figsize=(6, 6))
        height: int = self.maze.height
        width: int = self.maze.width

        # Iterate over each cell in the maze grid.
        for r in range(height):
            for c in range(width):
                cell = self.maze.grid[r][c]
                x: int = c
                y: int = r

                # Draw walls
                if cell.walls.get("top", True):
                    ax.plot([x, x + 1], [y, y], color="black")
                if cell.walls.get("bottom", True):
                    ax.plot([x, x + 1], [y + 1, y + 1], color="black")
                if cell.walls.get("left", True):
                    ax.plot([x, x], [y, y + 1], color="black")
                if cell.walls.get("right", True):
                    ax.plot([x + 1, x + 1], [y, y + 1], color="black")

        # Mark the entry (start) in green
        start_x, start_y = 0, 0
        ax.scatter(start_x + 0.5, start_y + 0.5, color="green", s=200, label="Entry (Start)")

        # Mark the exit (goal) in blue
        goal_x, goal_y = width - 1, height - 1
        ax.scatter(goal_x + 0.5, goal_y + 0.5, color="blue", s=200, label="Exit (Goal)")

        # Optionally draw the solution path, if provided.
        if path:
            x_coords: List[float] = [c + 0.5 for (r, c) in path]
            y_coords: List[float] = [r + 0.5 for (r, c) in path]
            ax.plot(x_coords, y_coords, color="red", linewidth=2, marker="o", label="Solution Path")

        # Set up the plot
        ax.set_aspect("equal")
        ax.set_xlim(0, width)
        ax.set_ylim(0, height)
        ax.invert_yaxis()
        ax.axis("off")
        ax.legend(loc="upper right")
        plt.show()

