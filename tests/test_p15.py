from aoc20.p15 import parse_input, nth_number


def test_example():
    data = """
0,3,6
""".strip().splitlines()
    assert nth_number(parse_input(data)) == 436
