#!/bin/bash

echo "Welcome to MazeGenSol"

echo -n "Visualize Maze? [y/n]:"
read -r ans

if [ "$ans" == "y" ]; then
  python main.py --size 140 --visualize --algorithm astar 
else
  python main.py --size 190 --algorithm astar 
  python main.py --size 190 --algorithm bfs
  python main.py --size 190 --algorithm dfs
fi

