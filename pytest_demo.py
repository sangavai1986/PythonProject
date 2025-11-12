import pytest


@pytest.mark.smoke
def test_addition():
    print("Addition")
    assert 1 + 1 == 2

@pytest.mark.re
def test_subtraction():
    assert 5 - 2 == 3

@pytest.mark.smoke
def test_multiplication():
    print("multi")
    assert 2 * 3 == 6

def test_division():
    assert 10 / 2 == 5

def test_string_concat():
    assert "hello" + "world" == "helloworld"

def test_list_append():
    my_list = [1, 2]
    my_list.append(3)
    assert my_list == [1, 2, 3]