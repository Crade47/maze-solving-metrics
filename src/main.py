import argparse
# import time
# import csv
from maze import Maze


def main():
    print("Welcome to Maze solver")

    parser = argparse.ArgumentParser(description="Maze Solver AI")
    parser.add_argument("--size", type=int, required=True, help="Maze size (N x N)")

    args = parser.parse_args()
    maze = Maze(args.size)  

    maze.generate()
    maze.display()

if __name__ == "__main__":
    main()
