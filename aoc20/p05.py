from aoc20 import utils


def parse_passes(passes: list[str]) -> list[int]:
    table = str.maketrans(
        {
            "F": "0",
            "B": "1",
            "R": "1",
            "L": "0",
        }
    )
    return [int(s.translate(table), 2) for s in passes]


def max_pass_id(passes: list[str]) -> int:
    return max(parse_passes(passes))


def find_our_seat(passes: list[str]) -> int:
    prev, *rest = sorted(parse_passes(passes))
    for cur in rest:
        if cur != prev + 1:
            return prev + 1
        prev = cur
    raise ValueError("Our seat in between is not found")


def parse_input(lines: list[str]) -> list[str]:
    return lines


def main() -> None:
    passes = parse_input(utils.read_input_lines(__file__))
    print(max_pass_id(passes))
    print(find_our_seat(passes))


if __name__ == "__main__":
    main()
