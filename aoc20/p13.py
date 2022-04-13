import math
from aoc20 import utils


def id_by_wait_time(earliest: int, buses: dict[int, int]) -> int:
    bus, time = min(
        ((bus, (bus - earliest) % bus) for bus in buses),
        key=lambda t: t[1],
    )
    return bus * time


def chinese_remainder(ns: list[int], rs: list[int]) -> int:
    p = math.prod(ns)
    ms = [p // n for n in ns]
    return sum(r * m * pow(m, -1, n) for m, n, r in zip(ms, ns, rs)) % p


def earliest_departure(buses: dict[int, int]) -> int:
    ns, rs = zip(*[(k, (k - v) % k) for k, v in buses.items()])
    return chinese_remainder(list(ns), list(rs))


def parse_input(lines: list[str]) -> tuple[int, dict[int, int]]:
    earliest, buses = lines
    delays = {int(s): i for i, s in enumerate(buses.split(",")) if s != "x"}
    return int(earliest), delays


def main() -> None:
    earliest, buses = parse_input(utils.read_input_lines(__file__))
    print(id_by_wait_time(earliest, buses))
    print(earliest_departure(buses))


if __name__ == "__main__":
    main()
