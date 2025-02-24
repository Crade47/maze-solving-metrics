from typing import List
from maze.maze import Maze
from utils.types import CoordinateType


class VI_MDP:
    def __init__(
        self, maze: Maze, gamma: float = 0.9, move_cost: int = -1, goal_reward=10, max_iter = 1000
    ):
        """
        Initialize the MDP for maze solving.

        Parameters:
        - maze: a Maze object with attributes width, height, and grid.
        - gamma: discount factor for future rewards.
        - move_cost: cost for each move (usually a negative value).
        - goal_reward: reward for reaching the goal state.
        """
        self.maze: Maze = maze
        self.gamma: float = gamma
        self.move_cost: int = move_cost
        self.goal_reward = goal_reward
        self.max_iter = max_iter

        self.values = {}
        self.policy = {}

        for r in range(self.maze.height):
            for c in range(self.maze.width):
                self.values[(r, c)] = 0.0
                self.policy[(r, c)] = None

        self.goal: CoordinateType = (self.maze.height - 1, self.maze.width - 1)

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

        # Check right movement (column +1)

        if c < self.maze.width - 1 and not cell.walls.get("right", True):
            actions.append((0, 1))
        # Check left movement (column -1)
        if c > 0 and not cell.walls.get("left", True):
            actions.append((0, -1))
        # Check down movement (row +1)
        if r < self.maze.height - 1 and not cell.walls.get("bottom", True):
            actions.append((1, 0))
        # Check up movement (row -1)
        if r > 0 and not cell.walls.get("top", True):
            actions.append((-1, 0))
        return actions

    def get_next_state(
        self, state: CoordinateType, action: CoordinateType
    ) -> CoordinateType:
        """
        Compute the next state given a state and an action.
        """
        r, c = state
        dr, dc = action
        return (r + dr, c + dc)

    def get_reward(self, next_state: CoordinateType) -> int:
        """
        Get the reward for the next state
        If next_state is the goal, return the goal reward; otherwise, return the move cost.
        """
        if next_state == self.goal:
            return self.goal_reward
        return -1

    def value_iteration(self, epsilon=0.001):
        """
        Perform value iteration untill the change in values is less than epsilon or
        the max_iterations is exhausted
        """

        iterations = 0
        while iterations < self.max_iter:
            delta = 0  # Maximum change in the value function in this iteration.
            new_values = self.values.copy()  # copy of the initialized values

            # iterate over all states and update it's values
            for state in self.values:
                if self.is_terminal(state):
                    new_values[state] = 0.0  # Terminal state value is 0
                    self.policy[state] = None
                    continue  # Skip to next state
                    
                best_value = float("-inf")
                best_action = None

                for action in self.get_actions(state):
                    next_state = self.get_next_state(state, action)
                    reward = self.get_reward(next_state)

                    value = reward + self.gamma * self.values[next_state]
                    if value > best_value:
                        best_value = value
                        best_action = action
                # if we reach a dead end
                if best_value == float("-inf"):
                    best_value = self.values[state]

                new_values[state] = best_value
                self.policy[state] = best_action
                delta = max(delta, abs(new_values[state] - self.values[state]))

            self.values = new_values
            iterations += 1

            if delta < epsilon:
                break

    def get_policy(self):
        """Return the computed policy after value iteration."""
        return self.policy

    def get_value_function(self):
        """Return the value function computed after value iteration."""
        return self.values

