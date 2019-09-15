""" 
Unit test for calculator
"""

from calculator import calculator


class TestCalculator:

    def test_add(self):
        print(dir(calculator.calculator))
        assert 4 == calculator.calculator.add(2, 2)

    def test_sub(self):
        assert 2 == calculator.calculator.sub(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.calculator.multiply(10, 10)