

class Robot:
    WIDTH = 101
    HEIGHT = 103
    def __init__(self, px, py, vx, vy) -> None:
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

    def move(self) -> None:
        self.px = (self.px + self.vx) % self.WIDTH
        self.py = (self.py + self.vy) % self.HEIGHT
        if self.px < 0:
            self.px = self.WIDTH - self.px

        if self.py < 0:
            self.py = self.HEIGHT - self.py
        
    def __str__(self) -> str:
        return f"({self.px},{self.py})"
