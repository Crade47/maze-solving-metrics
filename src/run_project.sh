#!/bin/bash

echo "Welcome to MazeGenSol"

echo -n "Visualize Maze? [y/n]:"
read -r ans

if [ "$ans" == "y" ]; then
  # python main.py --size 40 --visualize --algorithm astar 
    python main.py --size 30 --visualize --algorithm pi --gamma 0.9 --reward_goal 100 --reward_step -1  
    python main.py --size 30 --visualize --algorithm vi --gamma 0.9 --reward_goal 100 --reward_step -1 --max_iter 10000000  
else
    python main.py --size 100 --algorithm pi --gamma 0.99 --reward_goal 10000 --reward_step -1
    python main.py --size 100 --algorithm vi --gamma 0.9 --reward_goal 1000 --max_iter 100000 --reward_step -1  
    python main.py --size 100 --algorithm astar 
    python main.py --size 100 --algorithm bfs
    python main.py --size 100 --algorithm dfs
fi

