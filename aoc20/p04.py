import re
import typing

from aoc20 import utils


def is_present(entry: dict[str, str]) -> bool:
    required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    return all(field in entry for field in required)


def is_valid(entry: dict[str, str]) -> bool:
    regexps: dict[str, typing.Pattern[str]] = {
        "byr": re.compile(r"\d{4}$"),
        "iyr": re.compile(r"\d{4}$"),
        "eyr": re.compile(r"\d{4}$"),
        "hgt": re.compile(r"(\d+)(in|cm)$"),
        "hcl": re.compile(r"#[\da-f]{6}$"),
        "ecl": re.compile(r"(amb|blu|brn|gry|grn|hzl|oth)$"),
        "pid": re.compile(r"\d{9}$"),
    }
    rules: dict[str, typing.Callable[[typing.Match], bool]] = {
        "byr": lambda m: 1920 <= int(m.group(0)) <= 2002,
        "iyr": lambda m: 2010 <= int(m.group(0)) <= 2020,
        "eyr": lambda m: 2020 <= int(m.group(0)) <= 2030,
        "hgt": (
            lambda m: 150 <= int(m.group(1)) <= 193
            if m.group(2) == "cm"
            else 59 <= int(m.group(1)) <= 76
        ),
        "hcl": lambda m: True,
        "ecl": lambda m: True,
        "pid": lambda m: True,
    }
    for key in regexps:
        if key not in entry:
            return False
        value = entry[key]
        match = regexps[key].match(value)
        if not match:
            return False
        rule = rules[key]
        if not rule(match):
            return False
    return True


def count_valid_entries(entries: list[dict[str, str]]) -> int:
    return sum(1 for entry in entries if is_valid(entry))


def count_present_entries(entries: list[dict[str, str]]) -> int:
    return sum(1 for entry in entries if is_present(entry))


def parse_input(lines: list[str]) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    entry: dict[str, str] = {}
    for line in lines:
        if line:
            fields = line.split()
            in_fields = typing.cast(
                list[tuple[str, str]],
                [field.split(":", 1) for field in fields],
            )
            to_update: dict[str, str] = dict(in_fields)
            entry.update(to_update)
        else:
            entries.append(entry)
            entry = {}
    entries.append(entry)
    return entries


def main() -> None:
    entries = parse_input(utils.read_input_lines(__file__))
    print(count_present_entries(entries))
    print(count_valid_entries(entries))


if __name__ == "__main__":
    main()
