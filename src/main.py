import argparse
import time
from typing import Dict, Optional

# import csv
from algorithm.mdp.policy_iteration import PI_MDP
from algorithm.mdp.value_iteration import VI_MDP
from algorithm.search.bfs import BFS
from maze import Maze
from algorithm.search.dfs import DFS
from algorithm.search.astar import AStar
from utils import Visualizer
from utils.types import CoordinateType
from utils.utils import get_path_from_policy


def main():
    parser = argparse.ArgumentParser(description="Maze Solver AI")
    parser.add_argument("--size", type=int, required=True, help="Maze size (N x N)")
    parser.add_argument("--visualize", action="store_true", help="Visualize the Maze")
    parser.add_argument(
        "--algorithm",
        type=str,
        choices=["bfs", "dfs", "astar", "vi", "pi"],
        required=True,
        help="Algorithm used to solve the maze",
    )

    # mdp arguments
    parser.add_argument(
        "--reward_goal", type=int, help="Reward value for reaching the goal"
    )
    parser.add_argument("--reward_step", type=int, help="Step penalty (MDP Only)")
    parser.add_argument("--gamma", type=float, help="Discount Factor (MDP Only)")
    parser.add_argument("--max_iter", type=float, help="Maximum Iterations (MDP Only)")

    args = parser.parse_args()
    maze = Maze(args.size)
    maze.generate()
    path = []

    if args.algorithm in ["dfs", "bfs", "astar"]:
        start_time = time.time()

        if args.algorithm == "astar":
            solver = AStar(maze)
        if args.algorithm == "bfs":
            solver = BFS(maze)
        else:
            solver = DFS(maze)  # add a default algorithm rather than this

        path = solver.solve()
        exec_time = time.time() - start_time
        print(
            f"Execution time for ALGORITHM [{args.algorithm.capitalize()}] on SIZE: [{args.size} x {args.size}] : {exec_time}"
        )

    # if mdp algo is chosen
    else:
        start_time = time.time()

        if args.algorithm == "vi":
            solver = VI_MDP(
                maze,
                args.gamma,
                args.reward_step,
                args.reward_goal,
                args.max_iter
            )

            solver.value_iteration()
            policy: Dict[CoordinateType, Optional[CoordinateType]] = solver.get_policy()
            path = get_path_from_policy(policy, (0, 0), solver.goal)
            exec_time = time.time() - start_time
            print(
                f"Execution time for ALGORITHM [{args.algorithm.capitalize()}] on SIZE: [{args.size} x {args.size}] : {exec_time}"
            )

        if args.algorithm == "pi":
            solver = PI_MDP(
                maze,
                args.gamma,
                args.reward_step,
                args.reward_goal,
            )
            solver.policy_iteration()            
            policy: Dict[CoordinateType, Optional[CoordinateType]] = solver.get_policy()
            path = get_path_from_policy(policy, (0, 0), solver.goal)
            exec_time = time.time() - start_time
            print(
                f"Execution time for ALGORITHM [{args.algorithm.capitalize()}] on SIZE: [{args.size} x {args.size}] : {exec_time}"
            )

    if args.visualize:
        visualizer = Visualizer(maze)
        visualizer.visualize(path)


if __name__ == "__main__":
    main()
