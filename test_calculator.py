""" 
Unit test for calculator
"""

import calculator


class TestCalculator:

	def test_addition(self):
		assert 5 == calculator.add(2, 3)


	def test_substraction(self):

		assert 4 == calculator.sub(9, 5)

