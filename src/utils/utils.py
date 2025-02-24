
from typing import Dict, List, Optional, Tuple

from utils.types import CoordinateType


def reconstruct_path(
    came_from,
    start: Tuple[int, int],
    goal: Tuple[int, int],
) -> List[Tuple[int, int]]:
    path = []
    current = goal
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

def get_path_from_policy(
    policy: Dict[CoordinateType, Optional[CoordinateType]],
    start: CoordinateType,
    goal: CoordinateType,
) -> List[CoordinateType]:
    """
    Given a policy, return the path from start to goal, avoiding cycles.
    """
    path = [start]
    current = start
    max_steps = 1000  # Increased for larger mazes
    steps = 0
    visited = set()  # Track visited states to detect cycles

    while current != goal and steps < max_steps:
        if current in visited:
            print(f"Loop detected at {current}. Path may be incomplete.")
            break
        visited.add(current)
        
        action = policy.get(current)
        if action is None:
            print(f"No action at {current}. Path is incomplete.")
            break
        
        # Compute next state
        dr, dc = action
        r, c = current
        current = (r + dr, c + dc)
        path.append(current)
        steps += 1

    if current != goal:
        print(f"Warning: Path did not reach goal. Ended at {current}.")
    
    return path
