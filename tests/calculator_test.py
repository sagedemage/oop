"""Import the calculator class"""
import pytest

from calc.calculator import Calculator


def test_calculator_add():
    """Testing addition method"""
    # Adding two numbers
    assert Calculator.add_number(2, 3) == 5


def test_calculator_subtract():
    """Testing subtraction method"""
    # Subtracting two numbers
    assert Calculator.subtract_number(10, 5) == 5
