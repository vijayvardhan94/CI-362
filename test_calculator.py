"""
Unit tests for the calculator app
"""

import calculator


class TestCalculator:

    def test_add(self):
        assert 4 == calculator.add(2, 2)

    def test_subtract(self):
        assert 2 == calculator.subtract(4, 2)