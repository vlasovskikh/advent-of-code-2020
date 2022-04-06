import functools
import operator

from aoc20 import utils


def count_any_yes(group: list[str]) -> int:
    sets = (set(person) for person in group)
    return len(functools.reduce(operator.or_, sets))


def count_all_yes(group: list[str]) -> int:
    sets = (set(person) for person in group)
    return len(functools.reduce(operator.and_, sets))


def count_any_yes_in_groups(groups: list[list[str]]) -> int:
    return sum(count_any_yes(group) for group in groups)


def count_all_yes_in_groups(groups: list[list[str]]) -> int:
    return sum(count_all_yes(group) for group in groups)


def parse_input(lines: list[str]) -> list[list[str]]:
    groups: list[list[str]] = []
    group: list[str] = []
    for line in lines:
        if line:
            group.append(line)
        else:
            groups.append(group)
            group = []
    groups.append(group)
    return groups


def main() -> None:
    groups = parse_input(utils.read_input_lines(__file__))
    print(count_any_yes_in_groups(groups))
    print(count_all_yes_in_groups(groups))


if __name__ == "__main__":
    main()
