from aoc20.p22 import parse_input, play_crab_combat, play_recursive_combat


def test_example():
    data = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
""".strip().splitlines()
    assert play_crab_combat(*parse_input(data)) == 306


def test_recursive():
    data = """
    Player 1:
    9
    2
    6
    3
    1

    Player 2:
    5
    8
    4
    7
    10
    """.strip().splitlines()
    assert play_recursive_combat(*parse_input(data)) == 291
