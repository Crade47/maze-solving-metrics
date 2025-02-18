import argparse
import time
# import csv
from algorithm.search.bfs import BFS
from maze import Maze
from algorithm.search.dfs import DFS
from utils import Visualizer


def main():

    parser = argparse.ArgumentParser(description="Maze Solver AI")
    parser.add_argument("--size", type=int, required=True, help="Maze size (N x N)")
    parser.add_argument("--visualize", action="store_true", help="Visualize the Maze")
    parser.add_argument("--algorithm", type=str, choices=["bfs", "dfs"],required=True, help="Algorithm used to solve the maze")

    args = parser.parse_args()
    maze = Maze(args.size)  
    maze.generate()
    path = []



    if args.algorithm in ["dfs", "bfs", "astar"]:
        start_time = time.time()
 
        if args.algorithm == "bfs":
            solver = BFS(maze)
        else: 
            solver = DFS(maze) #add a default algorithm rather than this


        path = solver.solve()
        exec_time = time.time() - start_time
        print(f"Execution time for algorithm {args.algorithm.capitalize()}: {exec_time}")

    if args.visualize:
        visualizer = Visualizer(maze)
        visualizer.visualize(path)

if __name__ == "__main__":
    main()
