import re
from dataclasses import dataclass
from typing import Optional

from aoc20 import utils


class Instruction:
    pass


@dataclass
class Mask(Instruction):
    value: str

    def apply(self, n: int) -> int:
        set_ones_mask = int(self.value.replace("X", "0"), 2)
        reset_zeros_mask = int(self.value.replace("X", "1"), 2)
        return (n | set_ones_mask) & reset_zeros_mask

    def apply_v2(self, address: int) -> list[int]:
        set_ones_mask = int(self.value.replace("X", "0"), 2)
        reset_xs_mask = int(self.value.replace("0", "1").replace("X", "0"), 2)
        masked = (address | set_ones_mask) & reset_xs_mask
        indexes = [i for i, c in enumerate(reversed(self.value)) if c == "X"]
        n = len(indexes)
        result = []
        for x in range(2**n):
            s = masked
            for i in range(n):
                ith = x & (1 << i)  # i-th bit of x
                s |= ith << (indexes[i] - i)
            result.append(s)
        return result


@dataclass
class Mem(Instruction):
    address: int
    value: int


def initialize_memory(instructions: list[Instruction], *, v2: bool) -> int:
    memory: dict[int, int] = {}
    mask: Optional[Mask] = None
    for x in instructions:
        if isinstance(x, Mask):
            mask = x
        elif isinstance(x, Mem):
            if mask:
                if v2:
                    for address in mask.apply_v2(x.address):
                        memory[address] = x.value
                else:
                    memory[x.address] = mask.apply(x.value)
            else:
                memory[x.address] = x.value
        else:
            raise ValueError(f"Unknown instruction: {x}")
    return sum(memory.values())


def parse_input(lines: list[str]) -> list[Instruction]:
    result: list[Instruction] = []
    for line in lines:
        left, right = line.split(" = ")
        if left == "mask":
            result.append(Mask(right))
        elif m := re.match(r"mem\[(\d+)]", left):
            result.append(Mem(int(m.group(1)), int(right)))
        else:
            raise ValueError(f"Unknown command: {line}")
    return result


def main() -> None:
    instructions = parse_input(utils.read_input_lines(__file__))
    print(initialize_memory(instructions, v2=False))
    print(initialize_memory(instructions, v2=True))


if __name__ == "__main__":
    main()
