from aoc20.p08 import fix_and_execute, parse_input, execute


def test_example():
    data = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".strip().splitlines()
    assert execute(parse_input(data)) == (False, 5)


def test_fix_and_execute():
    data = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".strip().splitlines()
    assert fix_and_execute(parse_input(data)) == 8
