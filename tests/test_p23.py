import pytest

from aoc20.p23 import parse_input, play_crab_cups, play_many_cups


def test_example():
    data = """
389125467
""".strip().splitlines()
    assert play_crab_cups(parse_input(data)) == "67384529"


@pytest.mark.slow
def test_many_cups():
    data = """
389125467
""".strip().splitlines()
    assert play_many_cups(parse_input(data)) == 149245887792
