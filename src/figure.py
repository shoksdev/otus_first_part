from typing import Type, Self
from abc import ABC, abstractmethod


class Figure(ABC):
    """Базовый класс для всех фигур"""

    @property
    @abstractmethod
    def area(self):
        """Свойство для рассчета площади фигуры"""
        pass

    @property
    @abstractmethod
    def perimeter(self):
        """Свойство для рассчета периметра фигуры"""
        pass

    def add_area(self, figure: Type[Self]):
        """Метод для сложения площади фигур"""
        if not isinstance(figure, Figure):
            raise ValueError
        return self.area + figure.area
