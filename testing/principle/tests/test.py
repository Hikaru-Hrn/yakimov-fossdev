"""
Демонтрация тестов программы на наличее ошибок
"""

import sys
sys.path.append("src")

from math_demo import(
    add, add_with_bug, tax_calculator_bugged
)

def test_addition():
    assert add(2, 2) == 4
    print("test_addition good")

def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(0, 0) == 0

    print("test_addition_with_bug good")

def test_addition_dublicate():
    assert add(6, 7) == 6 + 7
    print("test_addition_dublicate good")


def test_addition_clusters():
    assert add(7, 6) == 13
    assert add(0, 6) == 6
    assert add(7, 0) == 7
    assert add(10, -11) == -1
    print("test_addition_clusters good")

# Trash
def test_addition_overkill():
    for i in range(0, 2**32):
        for j in range(0, 2**32):
            assert add(i, j) == i + j


def test_addition_culculator_bug():
    assert tax_calculator_bugged(1000) == 150
    assert tax_calculator_bugged(100) == 15
    assert tax_calculator_bugged(10) == 1.5
    assert tax_calculator_bugged(2.34) == 0.35

    print("test_addition_culculator_bug good")

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_dublicate()
    test_addition_clusters()
    test_addition_culculator_bug()
