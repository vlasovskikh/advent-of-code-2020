from aoc20.p13 import parse_input, id_by_wait_time, earliest_departure


def test_example():
    data = """
939
7,13,x,x,59,x,31,19
""".strip().splitlines()
    assert id_by_wait_time(*parse_input(data)) == 295


def test_offsets_1():
    data = """
0
17,x,13,19
""".strip().splitlines()
    _, buses = parse_input(data)
    assert earliest_departure(buses) == 3417


def test_offsets_2():
    data = """
0
1789,37,47,1889
""".strip().splitlines()
    _, buses = parse_input(data)
    assert earliest_departure(buses) == 1202161486
