from aoc20.p14 import parse_input, initialize_memory


def test_example():
    data = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
""".strip().splitlines()
    assert initialize_memory(parse_input(data), v2=False) == 165


def test_example_v2():
    data = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
""".strip().splitlines()
    assert initialize_memory(parse_input(data), v2=True) == 208
