from aoc20 import utils


def execute(instructions: list[tuple[str, int]]) -> tuple[bool, int]:
    ip, acc = 0, 0
    seen: set[int] = set()
    while True:
        if ip in seen:
            return False, acc
        seen.add(ip)
        if ip >= len(instructions):
            return True, acc
        op, arg = instructions[ip]
        if op == "acc":
            acc += arg
            ip += 1
        elif op == "jmp":
            ip += arg
        elif op == "nop":
            ip += 1
        else:
            raise ValueError(f"Unknown instruction: '{op}'")


def fix_and_execute(instructions: list[tuple[str, int]]) -> int:
    to_change = (i for i, (op, _) in enumerate(instructions) if op in ("nop", "jmp"))
    for i in to_change:
        copy = instructions.copy()
        op, arg = copy[i]
        new_op = "jmp" if op == "nop" else "nop"
        copy[i] = new_op, arg
        res, acc = execute(copy)
        if res:
            return acc
    raise ValueError("Cannot fix the program")


def parse_input(lines: list[str]) -> list[tuple[str, int]]:
    instructions: list[tuple[str, int]] = []
    for line in lines:
        op, arg = line.split()
        instructions.append((op, int(arg)))
    return instructions


def main() -> None:
    instructions = parse_input(utils.read_input_lines(__file__))
    print(execute(instructions))
    print(fix_and_execute(instructions))


if __name__ == "__main__":
    main()
