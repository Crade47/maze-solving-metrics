# Maze solver


## 1. Implementation (30%)

### Step 1.1: Maze Generator
- Research open-source Python maze generators (e.g., pyamaze or recursive backtracking).
- Ensure the chosen code is compatible with the project’s license (e.g., MIT, Apache) and credit it in the report.
- Modify the generator to produce mazes of varying sizes (e.g., 10x10, 20x20, 50x50) without hardcoding dimensions.

### Step 1.2: Search Algorithms
- Implement DFS and BFS using stacks/queues to traverse the maze.
- Implement A* with a heuristic (e.g., Manhattan distance) for pathfinding.

### Step 1.3: MDP Algorithms
- Model the maze as an MDP with:
  - States (cells)
  - Actions (movements)
  - Transitions (probabilities)
  - Rewards (goal = +100, traps = -50, steps = -1)
- Implement Value Iteration and Policy Iteration with a discount factor (e.g., γ = 0.9).

### Step 1.4: Code Quality
- Modularize code (e.g., separate files for maze generation, search, MDP).
- Add comments, docstrings, and ensure no hardcoding.
- Test edge cases (e.g., no valid path).
