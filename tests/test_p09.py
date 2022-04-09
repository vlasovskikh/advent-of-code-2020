from aoc20.p09 import find_contiguous_weakness, parse_input, first_sum_mismatch


def test_example():
    data = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
""".strip().splitlines()
    assert first_sum_mismatch(parse_input(data), 5) == 127


def test_weakness():
    data = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
""".strip().splitlines()
    numbers = parse_input(data)
    mismatch = first_sum_mismatch(numbers, 5)
    assert find_contiguous_weakness(numbers, mismatch) == 62
