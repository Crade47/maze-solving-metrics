#!/usr/bin/env python3
import csv
import time
from typing import Dict, List, Optional, Tuple

# Import your Maze and solver classes.
from maze import Maze
from algorithm.search.bfs import BFS
from algorithm.search.dfs import DFS
from algorithm.search.astar import AStar
from algorithm.mdp.value_iteration import VI_MDP
from algorithm.mdp.policy_iteration import PI_MDP
from utils.types import CoordinateType
from utils.utils import get_path_from_policy

def run_experiment(
    algorithm: str, 
    maze_size: int, 
    mdp_args
) -> Tuple[float, Optional[List[CoordinateType]]]:
    """
    Run a specific algorithm on a maze of given size.
    
    Parameters:
    - algorithm: one of "bfs", "dfs", "astar", "vi", or "pi".
    - maze_size: the dimension (N x N) of the maze.
    - mdp_args: parameters for MDP algorithms (gamma, reward_goal, reward_step, max_iter).

    Returns:
    - A tuple of (execution_time, path), where path is a list of (row, col) coordinates.
    """
    maze: Maze = Maze(maze_size)
    maze.generate()
    start_time: float = time.time()
    path: Optional[List[CoordinateType]] = None

    if algorithm in ["bfs", "dfs", "astar"]:
        if algorithm == "astar":
            solver = AStar(maze)
        elif algorithm == "bfs":
            solver = BFS(maze)
        else:
            solver = DFS(maze)
        path = solver.solve()
    elif algorithm == "vi":
        solver = VI_MDP(
            maze,
            gamma=mdp_args.get("gamma", 0.9),
            move_cost=mdp_args.get("reward_step", -1),
            goal_reward=mdp_args.get("reward_goal", 10) * maze_size,
            max_iter=int(mdp_args.get("max_iter", 100000))
        )
        solver.value_iteration()
        # For VI, obtain the policy and derive the path.
        policy: Dict[CoordinateType, Optional[CoordinateType]] = solver.get_policy()
        path = get_path_from_policy(policy, (0, 0), solver.goal)
    elif algorithm == "pi":
        solver = PI_MDP(
            maze,
            gamma=mdp_args.get("gamma", 0.9),
            move_cost=mdp_args.get("reward_step", -1),
            goal_reward=mdp_args.get("reward_goal", 10)
        )
        solver.policy_iteration()
        # For PI, obtain the policy and derive the path.
        policy: Dict[CoordinateType, Optional[CoordinateType]] = solver.get_policy()
        path = get_path_from_policy(policy, (0, 0), solver.goal)
    
    exec_time: float = time.time() - start_time
    return exec_time, path

def main() -> None:
    # Define maze sizes: small, medium, and large.
    sizes: Dict[str, int] = {
        "small": 10,   # For example, a 10x10 maze.
        "medium": 30,  # For example, a 30x30 maze.
        "large": 50   # For example, a 100x100 maze.
    }
    # List of algorithms to test.
    algorithms: List[str] = ["bfs", "dfs", "astar", "vi", "pi"]

    # Extra arguments for MDP algorithms.
    mdp_args: Dict[str, float] = {
        "gamma": 0.9,
        "reward_goal": 100,   # You may adjust these values as needed.
        "reward_step": -1,
        "max_iter": 100000
    }

    # Open a CSV file to store the batch experiment results.
    output_csv: str = "../data/batch_experiment_results.csv"
    with open(output_csv, mode="w", newline="") as csvfile:
        fieldnames: List[str] = ["Algorithm", "Maze_Size", "Execution_Time", "Path_Length"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Loop over each maze size and algorithm.
        for size_name, size in sizes.items():
            for alg in algorithms:
                print(f"Running {alg} on a {size_name} maze ({size} x {size})...")
                exec_time, path = run_experiment(alg, size, mdp_args)
                path_length: int = len(path) if path is not None else -1

                writer.writerow({
                    "Algorithm": alg,
                    "Maze_Size": size,
                    "Execution_Time": f"{exec_time:.6f}",
                    "Path_Length": path_length
                })
                print(f"Done: {alg} on {size} x {size} in {exec_time:.4f}s, path length: {path_length}")

    print(f"Batch experiment results saved to {output_csv}")

if __name__ == "__main__":
    main()

