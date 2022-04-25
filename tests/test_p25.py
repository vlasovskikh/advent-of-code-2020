from aoc20.p25 import parse_input, crack_encryption_key


def test_example():
    data = """
5764801
17807724
""".strip().splitlines()
    assert crack_encryption_key(*parse_input(data)) == 14897079
