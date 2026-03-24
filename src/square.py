from figure import Figure


class Square(Figure):
    """Класс квадрат"""

    def __init__(self, *args):
        self.side_a = args[0]

        if not isinstance(self.side_a, int):
            raise ValueError(
                f"Sides of square must be integer, now: side_a = {self.side_a}"
            )

    @property
    def area(self):
        return self.side_a**2

    @property
    def perimeter(self):
        return 4 * self.side_a
