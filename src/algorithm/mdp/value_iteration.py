from typing import List
from maze.maze import Maze
from utils.types import CoordinateType


class VI_MDP:
    def __init__(self, maze: Maze, gamma: float = 0.9, move_cost: int = -1, reward=10):
        """
        Initialize the MDP for maze solving.

        Parameters:
        - maze: a Maze object with attributes width, height, and grid.
        - gamma: discount factor for future rewards.
        - move_cost: cost for each move (usually a negative value).
        - goal_reward: reward for reaching the goal state.
        """
        self.maze: Maze = maze
        self.gamma: float = 0.9
        self.move_cost: int = -1
        self.reward = 10

        self.values = {}
        self.policy = {}

        for r in range(self.maze.height):
            for c in range(self.maze.width):
                self.values[(r, c)] = 0.0
                self.policy[(r, c)] = None

        self.goal: CoordinateType = (self.maze.width - 1, self.maze.height - 1)

    def is_terminal(self, state: tuple[int, int]) -> bool:
        """Check if a state is terminal (goal state)."""
        return state == self.goal

    def get_actions(self, state: CoordinateType) -> List[CoordinateType]:
        """
        Return the list of possible actions from a given state.
        Actions are represented as (dx, dy) tuples.
        Only moves allowed by the maze walls are returned.
        """
        actions: List[CoordinateType] = []
        r, c = state
        cell = self.maze.grid[r][c]

        if c < self.maze.width - 1:
        #check if moving right is allowed
            if not cell.walls.get("right", True):
                actions.append((0,1))
        #check if moving left is allowed
            if not cell.walls.get("left", True):
                actions.append((0, -1))
        if r < self.maze.width - 1:
        #check if moving up is allowed
            if not cell.walls.get("up", True):
                actions.append((-1, 0))
        #check if moving down is allowed
            if not cell.walls.get("down", True):
                actions.append((1, 0))
         

        return actions
    def get_next_state(self, state: CoordinateType, action: CoordinateType) -> CoordinateType:
        """
        Compute the next state given a state and an action.
        """
        r, c = state
        dr, dc = action
        return (r + dr, c + dc)

    def get_reward(self, state: CoordinateType, next_state: CoordinateType) -> int:
        """
            Get the reward for the next state
            If next_state is the goal, return the goal reward; otherwise, return the move cost.
        """
        if next_state == self.goal:
            return 10
        return -1

    def value_iteration(self, epsilon=0.001, max_iterations=1000):
        """
            Perform value iteration untill the change in values is less than epsilon or
            the max_iterations is exhausted
        """



