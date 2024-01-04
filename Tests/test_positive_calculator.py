import pytest

from app.calculator import Calculator

class TestCalculator:

    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 5, 25) == 30

    def test_multiply_success(self):
        assert self.calc.multiply(self, 100, 5) == 500

    def test_division_success(self):
        assert self.calc.division(self, 2, 2) == 1

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 60, 25) == 35

    def teardown(self):
        print('Выполнение метода Teardown')