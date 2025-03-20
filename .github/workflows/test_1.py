
import pytest

def square(n):
    return n**2

def cube(n):
    return n**3

def fifth_power(n):
    return n**5

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16
    
def test_cube():
    assert cube(2) == 8
    assert cube(3) == 27
    assert cube(4) == 64

def test_fifth_power():
    assert fifth_power(2) == 32
    assert fifth_power(3) == 243
    assert fifth_power(4) == 1024
    
def test_invalid_input():
    with pytest.raises(TypeError):
        square('a')
        cube('a')
        fifth_power('a')
