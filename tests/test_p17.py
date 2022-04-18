from aoc20.p17 import parse_input, simulate


def test_example_3():
    data = """
.#.
..#
###
""".strip().splitlines()
    assert simulate(parse_input(data), 3) == 112


def test_example_4():
    data = """
.#.
..#
###
""".strip().splitlines()
    assert simulate(parse_input(data), 4) == 848
