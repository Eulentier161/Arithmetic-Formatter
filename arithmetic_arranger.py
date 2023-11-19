from functools import cached_property
from typing import Literal


class BadOperator(Exception):
    pass


class NumberTooBig(Exception):
    pass


class Problem:
    def __init__(self, n1: str, operator: str, n2: str):
        self.n1 = int(n1)
        self.n2 = int(n2)
        self.n_width = max(len(n1), len(n2))
        if self.n_width > 4:
            raise NumberTooBig()
        if operator not in "+-":
            raise BadOperator()
        self.max_width = self.n_width + 2
        self.operator: Literal["+", "-"] = operator

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

    lines = [[], [], []]
    if include_result:
        lines.append([])
    for problem in parsed_problems:
        lines[0].append(f"{problem.n1:>{problem.max_width}}")
        lines[1].append(f"{problem.operator} {problem.n2:>{problem.n_width}}")
        lines[2].append("-" * problem.max_width)
        if include_result:
            lines[3].append(f"{problem.result:>{problem.max_width}}")

    return "\n".join("    ".join(line) for line in lines)
