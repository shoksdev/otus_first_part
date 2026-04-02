from .figure import Figure


class Rectangle(Figure):
    """Класс прямоугольник"""

    def __init__(self, side_a: int | float, side_b: int | float):
        self.side_a = side_a
        self.side_b = side_b

        if not (
            (isinstance(self.side_a, int) or isinstance(self.side_a, float))
            and (isinstance(self.side_b, int) or isinstance(self.side_b, float))
        ):
            raise ValueError(
                f"Sides of rectange must be integer or float, now: side_a = {self.side_a}, side_b = {self.side_b}"
            )

    @property
    def area(self):
        return self.side_a * self.side_b

    @property
    def perimeter(self):
        return 2 * (self.side_a + self.side_b)
