from aoc20.p11 import parse_input, count_seats_at_fixed_point


def test_adjacent():
    data = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".strip().splitlines()
    assert count_seats_at_fixed_point(parse_input(data), use_visible=False) == 37


def test_visible():
    data = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
    """.strip().splitlines()
    assert count_seats_at_fixed_point(parse_input(data), use_visible=True) == 26
