import math
from figure import Figure


class Triangle(Figure):
    """Класс треугольник"""

    def __init__(self, side_a: int | float, side_b: int | float, side_c: int | float):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        if not (
            (isinstance(self.side_a, int) or isinstance(self.side_a, float))
            and (isinstance(self.side_b, int) or isinstance(self.side_b, float))
            and (isinstance(self.side_c, int) or isinstance(self.side_c, float))
        ):
            raise ValueError(
                f"Sides of triangle must be integer or float, now: side_a = {self.side_a}, side_b = {self.side_b}, side_c = {self.side_c}"
            )

        if not (
            self.side_a + self.side_b > self.side_c
            and self.side_a + self.side_c > self.side_b
            and self.side_b + self.side_c > self.side_a
        ):
            raise ValueError(
                f"A triangle with such sides does not exist: {self.side_a}, {self.side_b}, {self.side_c}"
            )

    @property
    def area(self):
        p = self.perimeter / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
