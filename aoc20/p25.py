import itertools
from typing import Iterable

from aoc20 import utils


def transform(subject_number: int) -> Iterable[int]:
    value = 1
    while True:
        value = (value * subject_number) % 20_201_227
        yield value


def crack_encryption_key(pub_key_1: int, pub_key_2: int) -> int:
    keys = {pub_key_1, pub_key_2}
    loop_size, value = next((i, v) for i, v in enumerate(transform(7)) if v in keys)
    next_key = pub_key_1 if value == pub_key_2 else pub_key_2
    return next(itertools.islice(transform(next_key), loop_size, loop_size + 1))


def parse_input(lines: list[str]) -> tuple[int, int]:
    pub_key_1, pub_key_2 = [int(line) for line in lines]
    return pub_key_1, pub_key_2


def main() -> None:
    pub_keys = parse_input(utils.read_input_lines(__file__))
    print(crack_encryption_key(*pub_keys))


if __name__ == "__main__":
    main()
