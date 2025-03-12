from typing import Tuple

from dto.equation import Equation
from dto.result import Result


class Method:
    name = None

    def __init__(self, equation: Equation, left: float, right: float,
                 eps: float, decimal_places: int):
        self.decimal_places = decimal_places
        self.eps = eps
        self.right = right
        self.left = left
        self.equation = equation

    def solve(self) -> Result:
        pass

    def check(self) -> Tuple[bool, str]:
        return True, ''
