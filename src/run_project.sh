#!/bin/bash

echo "Welcome to MazeGenSol"

echo -n "Visualize Maze? [y/n]:"
read -r ans

if [ "$ans" == "y" ]; then
  python main.py --size 20 --visualize --algorithm dfs 
else
  python main.py --size 10 --algorithm bfs
  python main.py --size 10 --algorithm dfs
fi

