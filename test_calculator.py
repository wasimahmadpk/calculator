# Unit test for calculator


import calculator


class TestCalculator:

    def test_add(self):
        assert 4 == calculator.add(2, 2)

    def test_sub(self):
        assert 2 == calculator.sub(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
    	assert 5 == calculator.divide(50, 10)
