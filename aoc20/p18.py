import operator
from dataclasses import dataclass
from enum import Enum
from typing import Callable, Union

from funcparserlib.lexer import Token, make_tokenizer
from funcparserlib.parser import tok, Parser, forward_decl, finished, many

from aoc20 import utils


@dataclass
class BinaryExpr:
    op: str
    left: "Expr"
    right: "Expr"


Expr = Union[BinaryExpr, int]


class Priority(Enum):
    FLAT = 1
    ADD = 2


def tokenize(s: str) -> list[Token]:
    specs = [
        ("space", (r"\s+",)),
        ("num", (r"\d+",)),
        ("op", (r"[+*()]",)),
    ]
    f = make_tokenizer(specs)
    return [t for t in f(s) if t.type != "space"]


def op(name: str) -> Parser:
    return tok("op", name)


def to_expr(args: tuple[int, list[tuple[str, int]]]) -> Expr:
    first, rest = args
    result: Expr = first
    for op_, expr in rest:
        result = BinaryExpr(op_, result, expr)
    return result


def parse(s: str, priority: Priority) -> Expr:
    num = tok("num") >> int
    expr = forward_decl()  # type: Parser[Token, Expr]
    parenthesized = -op("(") + expr + -op(")")
    bin_op = op("*") | op("+")
    simple = num | parenthesized
    if priority == Priority.FLAT:
        bin_expr = simple + many(bin_op + simple) >> to_expr
        expr.define(bin_expr | simple)
    elif priority == Priority.ADD:
        add_expr = simple + many(op("+") + simple) >> to_expr
        mul_expr = add_expr + many(op("*") + add_expr) >> to_expr
        expr.define(mul_expr | simple)
    else:
        raise ValueError(f"Unknown priority: {priority!r}")
    document = expr + -finished

    return document.parse(tokenize(s))


def evaluate(expr: Expr) -> int:
    ops: dict[str, Callable[[int, int], int]] = {
        "+": operator.add,
        "*": operator.mul,
    }
    if isinstance(expr, int):
        return expr
    elif isinstance(expr, BinaryExpr):
        try:
            f = ops[expr.op]
        except KeyError:
            raise ValueError(f"Unknown operator {expr.op!r} in {expr}")
        return f(evaluate(expr.left), evaluate(expr.right))
    else:
        raise ValueError(f"Unknown expression: {expr!r}")


def sum_homework(expressions: list[Expr]) -> int:
    return sum(evaluate(expr) for expr in expressions)


def parse_input(lines: list[str], priority: Priority) -> list[Expr]:
    return [parse(line, priority) for line in lines]


def main() -> None:
    for _, priority in Priority.__members__.items():
        expressions = parse_input(utils.read_input_lines(__file__), priority)
        print(sum_homework(expressions))


if __name__ == "__main__":
    main()
