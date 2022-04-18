from aoc20.p18 import parse_input, sum_homework, Priority


def test_example_1():
    data = """
1 + 2 * 3 + 4 * 5 + 6
""".strip().splitlines()
    assert sum_homework(parse_input(data, Priority.FLAT)) == 71


def test_example_2():
    data = """
1 + (2 * 3) + (4 * (5 + 6))
""".strip().splitlines()
    assert sum_homework(parse_input(data, Priority.FLAT)) == 51


def test_example_3():
    data = """
2 * 3 + (4 * 5)
""".strip().splitlines()
    assert sum_homework(parse_input(data, Priority.FLAT)) == 26


def test_example_4():
    data = """
5 + (8 * 3 + 9 + 3 * 4 * 3)
""".strip().splitlines()
    assert sum_homework(parse_input(data, Priority.FLAT)) == 437


def test_example_5():
    data = """
1 + (2 * 3) + (4 * (5 + 6))
""".strip().splitlines()
    assert sum_homework(parse_input(data, Priority.ADD)) == 51


def test_example_6():
    data = """
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
""".strip().splitlines()
    assert sum_homework(parse_input(data, Priority.ADD)) == 23340
