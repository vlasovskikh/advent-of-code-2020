from aoc20.p06 import parse_input, count_any_yes_in_groups, count_all_yes_in_groups


def test_any():
    data = """
abc

a
b
c

ab
ac

a
a
a
a

b
""".strip().splitlines()
    assert count_any_yes_in_groups(parse_input(data)) == 11


def test_all():
    data = """
abc

a
b
c

ab
ac

a
a
a
a

b
""".strip().splitlines()
    assert count_all_yes_in_groups(parse_input(data)) == 6
