from src.rectangle import Rectangle
import pytest


@pytest.mark.parametrize(
    ('side_a', 'side_b', 'area', 'perimeter'),
    [
        pytest.param(3, 5, 15, 16, id='integer'),
        pytest.param(3.5, 5.5, 19.25, 18, id='float'),
    ],
)
def test_rectangle_area_perimeter_positive(side_a, side_b, area, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.area == area, f"Area of rectangle with sides {side_a} and {side_b} must be {area}, actual is {r.area}"
    assert r.perimeter == perimeter, f"Perimeter of rectangle with sides {side_a} and {side_b} must be {perimeter}, actual is {r.perimeter}"


@pytest.mark.parametrize(
    ('side_a', 'side_b'),
    [
        pytest.param(0, 5, id='zero'),
        pytest.param(-3, 5, id='negative side'),
        pytest.param(True, False, id='bool sides'),
        pytest.param('two', '7', id='string sides'),
        pytest.param([2], [3], id='list sides'),
        pytest.param(set([2]), set([3]), id='set sides'),
        pytest.param(tuple([1]), tuple([3]), id='tuple sides'),
        pytest.param('two', None, id='none side_b'),
    ],
)
def test_create_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)
