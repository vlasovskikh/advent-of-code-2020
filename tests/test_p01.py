from aoc20.p01 import parse_input, fix_expense_report


def test_example_pairs():
    data = """
1721
979
366
299
675
1456
""".strip().splitlines()
    assert fix_expense_report(parse_input(data), 2) == 514579


def test_example_triples():
    data = """
1721
979
366
299
675
1456
""".strip().splitlines()
    assert fix_expense_report(parse_input(data), 3) == 241861950
