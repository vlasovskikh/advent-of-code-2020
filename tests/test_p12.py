from aoc20.p12 import follow_waypoint, parse_input, follow_instructions


def test_example():
    data = """
F10
N3
F7
R90
F11
""".strip().splitlines()
    assert follow_instructions(parse_input(data)) == 25


def test_waypoint():
    data = """
F10
N3
F7
R90
F11
""".strip().splitlines()
    assert follow_waypoint(parse_input(data)) == 286
