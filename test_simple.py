from simple import si

def test_si_1():
    assert si(10, 5, 2) == 1

def test_si_2():
    assert si(10, 5, 4) == 2

def test_si_3():
    assert si(10, 10, 3) == 3
