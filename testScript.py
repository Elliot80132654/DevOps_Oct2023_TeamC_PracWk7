import pytest

def test_addition(a, b, expected):
    from calculator import add

    result = add(a, b)
    assert result == expected

def test_subtraction(a, b, expected):
    from calculator import subtract

    result = subtract(a, b)
    assert result == expected

def test_multiplication(a, b, expected):
    from calculator import multiply

    result = multiply(a, b)
    assert result == expected

def test_division(a, b, expected):
    from calculator import divide

    result = divide(a, b)
    assert result == expected

def test_cosine(angle, expected):
    from calculator import cosine

    result = cosine(angle)
    assert result == expected

def test_sine(angle, expected):
    from calculator import sine

    result = sine(angle)
    assert result == expected

def test_tangent(angle, expected):
    from calculator import tangent

    result = tangent(angle)
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (5.2, 3.1, 8.3),
    (-2, -3, -5),
    (100, -50, 50),
])
def test_addition_data(a, b, expected):
    test_addition(a, b, expected)

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, -1),
    (5.2, 3.1, 2.1),
    (-2, -3, 1),
    (100, -50, 150),
])
def test_subtraction_data(a, b, expected):
    test_subtraction(a, b, expected)

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (5.2, 3.1, 16.12),
    (-2, -3, 6),
    (100, 0.5, 50),
])
def test_multiplication_data(a, b, expected):
    test_multiplication(a, b, expected)

@pytest.mark.parametrize("a, b, expected", [
    (6, 2, 3),
    (16.12, 3.1, 5.2),
    (6, -3, -2),
])
def test_division_data(a, b, expected):
    test_division(a, b, expected)

@pytest.mark.parametrize("angle, expected", [
    (0, 1),
    (30, 0.8660254037844386),
    (45, 0.7071067811865476),
    (60, 0.5),
])
def test_cosine_data(angle, expected):
    test_cosine(angle, expected)

@pytest.mark.parametrize("angle, expected", [
    (0, 0),
    (30, 0.5),
    (45, 0.7071067811865475),
    (60, 0.8660254037844386),
])
def test_sine_data(angle, expected):
    test_sine(angle, expected)

@pytest.mark.parametrize("angle, expected", [
    (0, 0),
    (30, 0.5773502691920213),
    (45, 1),
    (60, 1.732050807568877),
])
def test_tangent_data(angle, expected):
    test_tangent(angle, expected)
