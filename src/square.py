from figure import Figure


class Square(Figure):
    """Класс квадрат"""

    def __init__(self, side_a: int | float):
        self.side_a = side_a

        if not (isinstance(self.side_a, int) or isinstance(self.side_a, float)):
            raise ValueError(
                f"Sides of square must be integer or float, now: side_a = {self.side_a}"
            )

    @property
    def area(self):
        return self.side_a**2

    @property
    def perimeter(self):
        return 4 * self.side_a
