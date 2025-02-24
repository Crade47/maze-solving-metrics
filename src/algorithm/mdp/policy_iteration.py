from typing import Dict, List, Optional
from maze.maze import Maze
from utils.types import CoordinateType


class PI_MDP:
    def __init__(
        self, maze: Maze, gamma: float = 0.9, move_cost: int = -1, goal_reward=10
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

        self.values: Dict[CoordinateType, float] = {}
        self.policy: Dict[CoordinateType, Optional[CoordinateType]] = {}

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

    def policy_evaluation(self, threshold: float = 1e-4) -> None:
        """Evaluates the current policy until values converge."""
        while True:
            delta: float = 0  # Track max change in value function
            new_values = self.values.copy()

            for state in self.values:
                if self.is_terminal(state):
                    continue  # Terminal states remain unchanged

                action = self.policy[state]
                if action is None:
                    continue  # No action assigned yet

                # Compute next state and determine reward
                next_state = self.get_next_state(state, action)
                is_terminal_next = self.is_terminal(next_state)
                reward = self.goal_reward if is_terminal_next else self.move_cost

                # Bellman equation: V(s) = R(s) + γ V(s')
                new_values[state] = reward + self.gamma * self.values.get(next_state, 0)

                delta = max(delta, abs(new_values[state] - self.values[state]))

            self.values = new_values  # Update state values

            if delta < threshold:
                break  # Stop when values converge

    def policy_improvement(self) -> bool:
        """Improves the policy based on updated values."""
        policy_stable = True

        for state in self.values:
            if self.is_terminal(state):
                continue  # Terminal state has no policy to update

            old_action = self.policy[state]
            best_action = None
            best_value = float("-inf")

            for action in self.get_actions(state):
                next_state = self.get_next_state(state, action)
                is_terminal_next = self.is_terminal(next_state)
                reward = self.goal_reward if is_terminal_next else self.move_cost
                value = reward + self.gamma * self.values.get(next_state, 0)

                if value > best_value:
                    best_value = value
                    best_action = action

            self.policy[state] = best_action

            if old_action != best_action:
                policy_stable = False  # Policy changed, not stable

        return policy_stable


    def policy_iteration(self):
        """Runs the policy iteration algorithm until convergence."""
        while True:
            self.policy_evaluation()
            if self.policy_improvement():
                break  # Stop if policy does not change

    def get_policy(self):
        """Return the computed policy after value iteration."""
        return self.policy

    def get_value_function(self):
        """Return the value function computed after value iteration."""
        return self.values

