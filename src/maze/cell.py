class Cell:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.walls = {
            "top": True,
            "right": True,
            "left": True,
            "bottom": True,
        }
