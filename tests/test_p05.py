from aoc20.p05 import parse_input, max_pass_id


def test_example():
    data = """
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
""".strip().splitlines()
    assert max_pass_id(parse_input(data)) == 820
