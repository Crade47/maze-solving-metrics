import argparse
# import time
# import csv
from algorithm.search.bfs import BFS
from maze import Maze
from utils import Visualizer


def main():

    parser = argparse.ArgumentParser(description="Maze Solver AI")
    parser.add_argument("--size", type=int, required=True, help="Maze size (N x N)")
    parser.add_argument("--visualize", type=bool, required=True, help="Visualize the Maze")

    args = parser.parse_args()
    maze = Maze(args.size)  
    generated_maze = maze.generate()


    solver = BFS(maze)
    path = solver.solve()
    print(path)

    if args.visualize:
        maze.display()
        visualizer = Visualizer(generated_maze)
        visualizer.visualize()
if __name__ == "__main__":
    main()
