# Sprint Plan: February 14 – February 28

**Submission Deadline:** February 28

## Overview
- **Goal:** Complete the project implementation, run experiments, finalize the report, and prepare the demo.
- **Focus Areas:**
  - Project structure setup and module implementation
  - Maze generation, search algorithms (DFS, BFS, A*), and MDP algorithms (Value & Policy Iteration)
  - Utilities, CLI/experiment integration, and testing
  - Documentation, report drafting, and demo preparation

---

## Week 1: February 14 – February 18

### Feb 14: Project Setup
- **Tasks:**
  - Initialize the repository and set up the project structure:
    - Create folders: `src/`, `data/`, `report/`, `demo/`
    - Add initial files: `readme.txt`, `requirements.txt`, `.gitignore`
  - Set up version control and branching strategy.

### Feb 15: Maze Generation Module
- **Tasks:**
  - Develop `src/maze/maze.py`:
    - Implement the `Maze` class with maze generation logic.
  - Develop `src/maze/cell.py`:
    - Implement the `Cell` class with walls and coordinates.
  - Write unit tests for maze generation functions.

### Feb 16: Search Algorithms Module
- **Tasks:**
  - Implement DFS and BFS:
    - Create `src/algorithms/search/dfs.py`
    - Create `src/algorithms/search/bfs.py`
  - Start implementing A* in `src/algorithms/search/astar.py`
  - Set up heuristic functions (e.g., Manhattan distance) in `src/utils/heuristics.py`

### Feb 17: MDP Algorithms Module
- **Tasks:**
  - Model the maze as an MDP (states, actions, transitions, rewards).
  - Implement Value Iteration in `src/algorithms/mdp/value_iteration.py`
  - Implement Policy Iteration in `src/algorithms/mdp/policy_iteration.py`

### Feb 18: Integration and Initial Testing
- **Tasks:**
  - Integrate maze generation with search and MDP modules.
  - Write integration tests to ensure modules work together.
  - Add basic documentation and inline comments.

---

## Week 2: February 19 – February 23

### Feb 19: Utilities & Experiment Runner
- **Tasks:**
  - Finalize helper modules:
    - Enhance `src/utils/heuristics.py` if needed.
    - Create `src/utils/visualizer.py` (using Matplotlib/Pygame).
    - Develop `src/utils/experiment_runner.py` for batch experiments and CSV logging.

### Feb 20: CLI & Experiment Integration
- **Tasks:**
  - Develop CLI entry points:
    - `src/main.py` for individual runs.
    - `src/experiment.py` for batch experiments.
  - Test CLI functionality and command-line arguments.

### Feb 21: Data Collection & Experiment Setup
- **Tasks:**
  - Run preliminary experiments and log results to CSV files in the `data/` folder.
  - Validate the functionality of the experiment runner and visualizer.
  - Refine the search and MDP algorithms based on initial experiment feedback.

### Feb 22: Code Refactoring & Documentation
- **Tasks:**
  - Refactor code for better modularity and clarity.
  - Add comprehensive comments and docstrings.
  - Ensure license compatibility and credit third-party libraries.

### Feb 23: Testing & Bug Fixing
- **Tasks:**
  - Conduct thorough unit and integration tests.
  - Identify and fix any bugs or edge-case issues.
  - Prepare a short test report detailing fixes and remaining issues.

---

## Week 3: February 24 – February 28

### Feb 24: Report Drafting & Appendices Preparation
- **Tasks:**
  - Begin drafting the main report (`report/report.pdf`):
    - Detail methodology, experiments, and analysis.
  - Prepare appendices with code snippets in `report/appendices/`.

### Feb 25: Demo Preparation
- **Tasks:**
  - Write a demo script in `demo/demo_script.txt`.
  - Start recording the demo video (`demo/demo.mp4`) highlighting key features.
  - Review and refine the demo content for clarity.

### Feb 26: Final Experiment Runs & Testing
- **Tasks:**
  - Run full-scale experiments to generate final results.
  - Finalize CSV data in the `data/` folder.
  - Re-run tests to ensure the code is stable and bug-free.

### Feb 27: Final Documentation & Report Revisions
- **Tasks:**
  - Finalize the report and appendices.
  - Update `readme.txt` with instructions for running the code.
  - Ensure all documentation, inline comments, and code quality standards are met.

### Feb 28: Final Review & Submission
- **Tasks:**
  - Conduct a final project review:
    - Verify the project structure and all functionalities.
    - Confirm experiment results and demo video are complete.
  - Submit the project by the deadline.

