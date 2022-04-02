from aoc20.p02 import parse_input, count_old_valid_passwords, count_new_valid_passwords


def test_old_example():
    data = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
""".strip().splitlines()
    assert count_old_valid_passwords(parse_input(data)) == 2


def test_new_example():
    data = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
""".strip().splitlines()
    assert count_new_valid_passwords(parse_input(data)) == 1
