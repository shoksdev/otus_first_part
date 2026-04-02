from src.triangle import Triangle
import pytest


@pytest.mark.parametrize(
    ('side_a', 'side_b', 'side_c', 'area', 'perimeter'),
    [
        pytest.param(3, 4,  5, 6.0, 12, id='integer'),
        pytest.param(3.5, 4.5, 5.5, 7.854885024620029, 13.5, id='float'),
    ],
)
def test_triangle_area_perimeter_positive(side_a, side_b, side_c, area, perimeter):
    r = Triangle(side_a, side_b, side_c)
    assert r.area == area, f"Area of triangle with sides {side_a} and {side_b} and {side_c} must be {area}, actual is {r.area}"
    assert r.perimeter == perimeter, f"Perimeter of triangle with sides {side_a} and {side_b} and {side_c} must be {perimeter}, actual is {r.perimeter}"


@pytest.mark.parametrize(
    ('side_a', 'side_b', 'side_c'),
    [
        pytest.param(0, 5, 7, id='zero'),
        pytest.param(-3, 5, 8,  id='negative side'),
        pytest.param(True, False, True, id='bool sides'),
        pytest.param('two', '7', 'three', id='string sides'),
        pytest.param([2], [3], [4], id='list sides'),
        pytest.param(set([2]), set([3]), set([4]), id='set sides'),
        pytest.param(tuple([1]), tuple([3]), tuple([4]), id='tuple sides'),
        pytest.param(2, None, 4, id='none side_b'),
        pytest.param(5, 3, 2, id='side_a + side_b > side_c'),
        pytest.param(2, 3, 5, id='side_a + side_c > side_b'),
        pytest.param(2, 5, 3, id='side_b + side_c > side_a'),
    ],
)
def test_create_triangle_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)
