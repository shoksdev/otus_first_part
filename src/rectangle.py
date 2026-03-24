from figure import Figure


class Rectangle(Figure):
    """Класс прямоугольник"""

    def __init__(self, *args):
        self.side_a = args[0]
        self.side_b = args[1]

        if not (isinstance(self.side_a, int) and isinstance(self.side_b, int)):
            raise ValueError(
                f"Sides of rectange must be integer, now: side_a = {self.side_a}, side_b = {self.side_b}"
            )

    @property
    def area(self):
        return self.side_a * self.side_b

    @property
    def perimeter(self):
        return 2 * (self.side_a + self.side_b)
