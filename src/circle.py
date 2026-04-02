import math
from .figure import Figure


class Circle(Figure):
    """Класс круг"""

    def __init__(self, radius: int | float):
        self.radius = radius

        if not (isinstance(self.radius, int) or isinstance(self.radius, float)):
            raise ValueError(
                f"Radius of square must be integer or float, now: radius = {self.radius}"
            )

    @property
    def area(self):
        return math.pi * self.radius**2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
