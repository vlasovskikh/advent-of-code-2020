import re
from typing import NamedTuple, Iterable

from aoc20 import utils


class PasswordEntry(NamedTuple):
    first: int
    second: int
    char: str
    password: str

    def is_old_valid(self) -> bool:
        return self.first <= self.password.count(self.char) <= self.second

    def is_new_valid(self) -> bool:
        c1 = self.password[self.first - 1]
        c2 = self.password[self.second - 1]
        return (self.char == c1) ^ (self.char == c2)


def count_old_valid_passwords(db: Iterable[PasswordEntry]) -> int:
    return sum(1 for entry in db if entry.is_old_valid())


def count_new_valid_passwords(db: Iterable[PasswordEntry]) -> int:
    return sum(1 for entry in db if entry.is_new_valid())


def parse_input(lines: list[str]) -> Iterable[PasswordEntry]:
    for line in lines:
        if m := re.match(r"(\d+)-(\d+) (\w): (\w+)", line):
            n_min, n_max, char, password = m.groups()
            yield PasswordEntry(int(n_min), int(n_max), char, password)


def main() -> None:
    db = list(parse_input(utils.read_input_lines(__file__)))
    print(count_old_valid_passwords(db))
    print(count_new_valid_passwords(db))


if __name__ == "__main__":
    main()
