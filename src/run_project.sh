#!/bin/bash

echo "Welcome to MazeGenSol"

echo -n "Visualize Maze? [y/n]:"
read -r ans

if [ "$ans" == "y" ]; then
  # python main.py --size 40 --visualize --algorithm astar 
  python main.py --size 140 --visualize --algorithm vi --gamma 0.9 --reward_goal 10000000000000000000000000000000000000000000000000 --max_iter 1000000 --reward_step -1  
else
  python main.py --size 190 --algorithm astar 
  python main.py --size 190 --algorithm bfs
  python main.py --size 190 --algorithm dfs
fi

