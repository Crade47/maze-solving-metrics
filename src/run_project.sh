#!/bin/bash

echo "Welcome to MazeGenSol"

echo -n "Visualize Maze? [y/n]:"
read -r ans

if [ "$ans" == "y" ]; then
  python main.py --size 4 --visualize True
else
  python main.py --size 4 
fi

