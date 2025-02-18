from maze import Maze
from algorithm.search.dfs import DFS


def test_dfs_simple_path():
    """
    Test DFS on a simple 2x2 maze with a clear path:

    Maze layout:
         Column 0   Column 1
    Row 0   (0,0)  --- (0,1)
             |           |
    Row 1   (1,0)  --- (1,1)

    Path: (0,0) -> (0,1) -> (1,1)
    """
    maze = Maze(2)
    # Remove wall between (0,0) and (0,1)
    maze.grid[0][0].walls["right"] = False
    maze.grid[0][1].walls["left"] = False
    # Remove wall between (0,1) and (1,1)
    maze.grid[0][1].walls["bottom"] = False
    maze.grid[1][1].walls["top"] = False
    solver = DFS(maze)
    path = solver.solve()
    expected_path = [(0, 0), (0, 1), (1, 1)]
    assert path == expected_path, f"Expected path {expected_path}, got {path}"


def test_dfs_no_path():
    """Test DFS when there is no valid path to the target (all walls intact)."""
    maze = Maze(2)
    # All walls remain intact by default
    solver = DFS(maze)
    path = solver.solve()
    assert path == [], "Expected empty path when no valid path exists"


def test_dfs_multiple_paths():
    """
    Test DFS with multiple possible paths to target:
    Path 1: (0,0) -> (0,1) -> (1,1)
    Path 2: (0,0) -> (1,0) -> (1,1)
    """
    maze = Maze(2)
    # Create path 1: right then down
    maze.grid[0][0].walls["right"] = False
    maze.grid[0][1].walls["left"] = False
    maze.grid[0][1].walls["bottom"] = False
    maze.grid[1][1].walls["top"] = False

    # Create path 2: down then right
    maze.grid[0][0].walls["bottom"] = False
    maze.grid[1][0].walls["top"] = False
    maze.grid[1][0].walls["right"] = False
    maze.grid[1][1].walls["left"] = False

    solver = DFS(maze)
    path = solver.solve()
    possible_paths = [[(0, 0), (0, 1), (1, 1)], [(0, 0), (1, 0), (1, 1)]]
    assert path in possible_paths, f"Path {path} not in expected paths {possible_paths}"


def test_dfs_larger_maze():
    """
    Test DFS on a 3x3 maze with a winding path:
    Path: (0,0) -> (0,1) -> (1,1) -> (1,2) -> (2,2)
    """
    maze = Maze(3)
    # Create winding path
    # (0,0) -> (0,1)
    maze.grid[0][0].walls["right"] = False
    maze.grid[0][1].walls["left"] = False
    # (0,1) -> (1,1)
    maze.grid[0][1].walls["bottom"] = False
    maze.grid[1][1].walls["top"] = False
    # (1,1) -> (1,2)
    maze.grid[1][1].walls["right"] = False
    maze.grid[1][2].walls["left"] = False
    # (1,2) -> (2,2)
    maze.grid[1][2].walls["bottom"] = False
    maze.grid[2][2].walls["top"] = False

    solver = DFS(maze)
    path = solver.solve()
    expected_path = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]
    assert path == expected_path, f"Expected path {expected_path}, got {path}"


def test_dfs_single_cell():
    """Test DFS on a 1x1 maze (edge case)."""
    maze = Maze(1)
    solver = DFS(maze)
    path = solver.solve()
    expected_path = [(0, 0)]
    assert path == expected_path, f"Expected path {expected_path}, got {path}"
