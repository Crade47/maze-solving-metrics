import argparse
# import time
# import csv
from maze import Maze
from utils import Visualizer


def main():

    parser = argparse.ArgumentParser(description="Maze Solver AI")
    parser.add_argument("--size", type=int, required=True, help="Maze size (N x N)")
    parser.add_argument("--visualize", type=bool, required=True, help="Visualize the Maze")

    args = parser.parse_args()
    maze = Maze(args.size)  
    generated_maze = maze.generate()
    if args.visualize:
        visualizer = Visualizer(generated_maze)
        visualizer.visualize()
if __name__ == "__main__":
    main()
