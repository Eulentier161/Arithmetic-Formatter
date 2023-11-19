from functools import cached_property
from typing import Literal


class BadOperator(Exception):
    pass


class NumberTooBig(Exception):
    pass


class Problem:
    def __init__(self, n1: str, operator: str, n2: str):
        if operator not in "+-":
            raise BadOperator()
        if len(n1) > 4 or len(n2) > 4:
            raise NumberTooBig()
        self.n1 = int(n1)
        self.n2 = int(n2)
        self.operator: Literal["+", "-"] = operator
        self.n_width = max(len(n1), len(n2))
        self.max_width = self.n_width + 2

    @cached_property
    def result(self):
        return self.n1 + self.n2 if self.operator == "+" else self.n1 - self.n2


def arithmetic_arranger(problems: list[str], include_result: bool = False):
    if len(problems) > 5:
        return "Error: Too many problems."

    try:
        parsed_problems = [Problem(*problem.split()) for problem in problems]
    except ValueError:
        return "Error: Numbers must only contain digits."
    except BadOperator:
        return "Error: Operator must be '+' or '-'."
    except NumberTooBig:
        return "Error: Numbers cannot be more than four digits."

    arranged_problems = "    ".join(f"{problem.n1:>{problem.max_width}}" for problem in parsed_problems)
    arranged_problems += "\n" + "    ".join(f"{problem.operator} {problem.n2:>{problem.n_width}}" for problem in parsed_problems)
    arranged_problems += "\n" + "    ".join("-" * problem.max_width for problem in parsed_problems)
    if include_result:
        arranged_problems += "\n" + "    ".join(f"{problem.result:>{problem.max_width}}" for problem in parsed_problems)

    return arranged_problems
