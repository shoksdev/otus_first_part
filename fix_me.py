"""Модуль содержащий функцию для расчета среднего значения"""


def calculate_average(numbers: list):
    """Функция для расчета среднего значения из переданного списка"""
    total = sum(numbers)
    count = len(numbers)
    return total / count


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
