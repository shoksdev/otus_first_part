import math
from figure import Figure


class Circle(Figure):
    """Класс круг"""

    def __init__(self, *args):
        self.radius = args[0]

        if not isinstance(self.radius, int):
            raise ValueError(
                f"Radius of square must be integer, now: radius = {self.radius}"
            )

    @property
    def area(self):
        return math.pi * self.radius**2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
