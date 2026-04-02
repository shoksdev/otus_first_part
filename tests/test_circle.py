from src.circle import Circle
import pytest


@pytest.mark.parametrize(
    ('radius', 'area', 'perimeter'),
    [
        pytest.param(3, 28.274333882308138, 18.84955592153876, id='integer'),
        pytest.param(3.5, 38.48451000647496, 21.991148575128552, id='float'),
    ],
)
def test_circle_area_perimeter_positive(radius, area, perimeter):
    r = Circle(radius)
    assert r.area == area, f"Area of circle with radius = {radius} must be {area}, actual is {r.area}"
    assert r.perimeter == perimeter, f"Perimeter of circle with radius = {radius} must be {perimeter}, actual is {r.perimeter}"


@pytest.mark.parametrize(
    ('radius'),
    [
        pytest.param(0, id='zero radius'),
        pytest.param(-3, id='negative radius'),
        pytest.param(True, id='bool radius'),
        pytest.param('two', id='string radius'),
        pytest.param([2], id='list radius'),
        pytest.param(set([2]), id='set radius'),
        pytest.param(tuple([1]), id='tuple radius'),
        pytest.param(None, id='none radius'),
    ],
)
def test_create_circle_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)
