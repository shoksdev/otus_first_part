from src.square import Square
import pytest


@pytest.mark.parametrize(
    ('side_a', 'area', 'perimeter'),
    [
        pytest.param(3, 9, 12, id='integer'),
        pytest.param(3.5, 12.25, 14.0, id='float'),
    ],
)
def test_square_area_perimeter_positive(side_a, area, perimeter):
    r = Square(side_a)
    assert r.area == area, f"Area of square with side_a = {side_a} must be {area}, actual is {r.area}"
    assert r.perimeter == perimeter, f"Perimeter of square with side_a = {side_a} must be {perimeter}, actual is {r.perimeter}"


@pytest.mark.parametrize(
    ('side_a'),
    [
        pytest.param(0, id='zero side_a'),
        pytest.param(-3, id='negative side_a'),
        pytest.param(True, id='bool side_a'),
        pytest.param('two', id='string side_a'),
        pytest.param([2], id='list side_a'),
        pytest.param(set([2]), id='set side_a'),
        pytest.param(tuple([1]), id='tuple side_a'),
        pytest.param(None, id='none side_a'),
    ],
)
def test_create_square_negative(side_a):
    with pytest.raises(ValueError):
        Square(side_a)
