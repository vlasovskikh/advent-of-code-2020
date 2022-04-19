import functools
import operator
from collections import defaultdict
from dataclasses import dataclass
from typing import cast, Union

from funcparserlib.lexer import make_tokenizer, Token
from funcparserlib.parser import (
    tok,
    oneplus,
    forward_decl,
    finished,
    many,
    Parser,
    NoParseError,
)

from aoc20 import utils


@dataclass
class SequenceExpr:
    children: list["Expr"]


@dataclass
class AlternativeExpr:
    children: list["Expr"]


Expr = Union[int, str, SequenceExpr, AlternativeExpr]


def tokenize_line(s: str) -> list[Token]:
    specs = [
        ("char", (r"\w",)),
    ]
    f = make_tokenizer(specs)
    return list(f(s))


def count_valid_lines(rules: dict[int, Expr], lines: list[str]) -> int:
    parser = to_parser(rules[0], rules) + -finished
    n = 0
    for line in lines:
        try:
            parser.parse(tokenize_line(line))
        except NoParseError:
            pass
        else:
            n += 1
    return n


def count_lines_after_updating(rules: dict[int, Expr], lines: list[str]) -> int:
    rules = rules.copy()
    # Non-greedy for (guess) ten matches of 42: "42*? 11"
    s = " | ".join([" ".join(["42"] * i) + " 11" for i in range(1, 11)])
    rules[0] = parse_expr(s)
    # rules[0] = parse_expr("42 11 | 42 42 11 | 42 42 42 11 | 42 42 42 42 11 | ...")
    # rules[0] = parse_expr("42 42* 42{1,n} 31{1,n}")
    # rules[8] = parse_expr("42 | 42 8")
    rules[11] = parse_expr("42 31 | 42 11 31")
    return count_valid_lines(rules, lines)


def to_str(s: str) -> str:
    return s[1:-1]


def to_sequence(args: list[Expr]) -> Expr:
    if not args:
        raise ValueError("Creating an empty sequence")
    elif len(args) == 1:
        return args[0]
    else:
        return SequenceExpr(args)


def to_alternative(args: tuple[Expr, list[Expr]]) -> Expr:
    first, rest = args
    if not rest:
        return first
    else:
        children = first, *rest
        return AlternativeExpr(cast(list, children))


def to_parser(expr: Expr, rules: dict[int, Expr]) -> "Parser[Token, str]":
    parsers: dict[int, "Parser[Token, str]"] = defaultdict(forward_decl)
    defined: set[int] = set()

    def f(e: Expr) -> "Parser[Token, str]":
        if isinstance(e, int):
            if e not in defined:
                defined.add(e)
                parsers[e].define(f(rules[e]))
                if not parsers[e].name.startswith('"'):
                    parsers[e].name = str(e)
            return parsers[e]
        elif isinstance(e, str):
            return tok("char", e)
        elif isinstance(e, SequenceExpr):
            return functools.reduce(operator.add, (f(c) for c in e.children))
        elif isinstance(e, AlternativeExpr):
            return functools.reduce(operator.or_, (f(c) for c in e.children))

    return f(expr)


def tokenize_expr(s: str) -> list[Token]:
    specs = [
        ("whitespace", (r"\s+",)),
        ("number", (r"\d+",)),
        ("string", (r'"\w+"',)),
        ("op", (r"[|]",)),
    ]
    f = make_tokenizer(specs)
    return [t for t in f(s) if t.type != "whitespace"]


def parse_expr(s: str) -> Expr:
    expr = forward_decl()  # type: Parser[Token, Expr]
    string = tok("string") >> to_str
    number = tok("number") >> int
    sequence = oneplus(number) >> to_sequence
    alternative = sequence + many(-tok("op", "|") + sequence) >> to_alternative
    expr.define(string | alternative)
    document = expr + -finished

    return document.parse(tokenize_expr(s))


def parse_input(lines: list[str]) -> tuple[dict[int, Expr], list[str]]:
    rules: dict[int, Expr] = {}
    state = "rules"
    res_lines: list[str] = []
    for line in lines:
        if state == "rules":
            if line:
                k, v = line.split(": ")
                rules[int(k)] = parse_expr(v)
            else:
                state = "lines"
        elif state == "lines":
            res_lines.append(line)
    return rules, res_lines


def main() -> None:
    rules, lines = parse_input(utils.read_input_lines(__file__))
    print(count_valid_lines(rules, lines))
    print(count_lines_after_updating(rules, lines))


if __name__ == "__main__":
    main()
