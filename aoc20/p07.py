import re
from collections import defaultdict

from aoc20 import utils


def count_gold_containers(containers: dict[str, list[tuple[int, str]]]) -> int:
    contents = containers_to_contents(containers)
    res: set[str] = set()
    queue = ["shiny gold"]
    while queue:
        color = queue.pop()
        new = contents[color] - res
        res.update(new)
        queue.extend(new)
    return len(res)


def count_gold_contents(containers: dict[str, list[tuple[int, str]]]) -> int:
    calculated: dict[str, int] = {}
    queue = ["shiny gold"]
    while queue:
        container = queue.pop()
        contents = containers[container]
        colors = {color for _, color in contents}
        if all(color in calculated for color in colors):
            calculated[container] = sum(
                number * (calculated[color] + 1) for number, color in contents
            )
        else:
            queue.append(container)
            for color in colors:
                if color not in calculated:
                    queue.append(color)
    return calculated["shiny gold"]


def containers_to_contents(
    containers: dict[str, list[tuple[int, str]]],
) -> dict[str, set[str]]:
    res: dict[str, set[str]] = defaultdict(set)
    for container, bags in containers.items():
        for _, color in bags:
            res[color].add(container)
    return res


def parse_input(lines: list[str]) -> dict[str, list[tuple[int, str]]]:
    containers: dict[str, list[tuple[int, str]]] = {}
    for line in lines:
        if m := re.match(r"(\w+ \w+) bags contain (.*)\.", line):
            container, contents = m.groups()
        else:
            raise ValueError(f"Cannot parse line: '{line}'")
        colors = contents.split(", ")
        bags: list[tuple[int, str]] = []
        for color in colors:
            if color == "no other bags":
                pass
            elif m := re.match(r"(\d+) (\w+ \w+) bags?", color):
                number, bag = m.groups()
                bags.append((int(number), bag))
            else:
                raise ValueError(f"Cannot parse color: '{color}'")
        containers[container] = bags
    return containers


def main() -> None:
    containers = parse_input(utils.read_input_lines(__file__))
    print(count_gold_containers(containers))
    print(count_gold_contents(containers))


if __name__ == "__main__":
    main()
