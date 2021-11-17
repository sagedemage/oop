""" content of calculator.py """
from calc.calculations.subtraction import Subtraction
from calc.calculations.addition import Addition


class Calculator:
    """Calculator class"""

    @staticmethod
    def add_number(value1, value2):
        """Add as many times to the first number"""
        addition = Addition.create(value1, value2)
        return addition.get_result()

    @staticmethod
    def subtract_number(value1, value2):
        """Subtract as many times to the first number"""
        subtraction = Subtraction.create(value1, value2)
        return subtraction.get_result()
