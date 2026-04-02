from src.square import Square
from src.rectangle import Rectangle
import pytest


@pytest.mark.parametrize(
    ('side_a', 'side_b', 'area'),
    [
        pytest.param(5, 3, 40, id='integer'),
        pytest.param(5.5, 3.5, 49.5, id='float'),
    ],
)
def test_add_area_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    s = Square(side_a)
    assert r.add_area(s) == area


@pytest.mark.parametrize(
    ('add_area'),
    [
        pytest.param(0, id='zero'),
        pytest.param(5, id='integer'),
        pytest.param(-5, id='negative area'),
        pytest.param(False, id='bool area'),
        pytest.param('7', id='string area'),
        pytest.param([3], id='list area'),
        pytest.param(set([3]), id='set area'),
        pytest.param(tuple([3]), id='tuple area'),
        pytest.param(None, id='none area'),
    ],
)
def test_add_area_positive(add_area):
    with pytest.raises(ValueError):
        s = Square(5)
        s.add_area(add_area)
