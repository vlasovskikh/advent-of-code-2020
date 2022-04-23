from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator, TypeVar, Generic, Iterable

from aoc20 import utils

T = TypeVar("T")


@dataclass(repr=False)
class Node(Generic[T]):
    value: T
    next: Node[T] | None

    @staticmethod
    def from_iterable(xs: Iterable[T], *, loop: bool = False) -> Node[T]:
        prev = None
        first = None
        for x in xs:
            n = Node(x, None)
            if prev:
                prev.next = n
            else:
                first = n
            prev = n
        if loop and prev is not None:
            prev.next = first
        if not first:
            raise ValueError("Cannot create a node from the empty iterable")
        return first

    def remove_next(self, count: int) -> Node[T]:
        node = self
        first = None
        for _ in range(count):
            n = node.next
            if not n:
                raise ValueError("Not enough elements in the node to remove")
            node = n
            if not first:
                first = node
        last = node
        self.next = last.next
        last.next = None
        if not first:
            raise ValueError("Cannot remove zero or less elements")
        return first

    def append(self, other: Node[T]) -> None:
        rest = self.next
        last = other
        while last.next:
            last = last.next
        self.next = other
        last.next = rest

    def __iter__(self) -> Iterator[T]:
        yield self.value
        n = self.next
        while n and n is not self:
            yield n.value
            n = n.next

    def __repr__(self) -> str:
        values = list(self)
        return f"Node.from_iterable({values}, ...)"


@dataclass(init=False)
class Circle:
    current: Node[int]
    values: dict[int, Node[int]]

    def __init__(self, xs: list[int]) -> None:
        self.current = Node.from_iterable(xs, loop=True)
        self.values = {}
        node = self.current
        for _ in range(len(xs)):
            self.values[node.value] = node
            n = node.next
            assert n
            node = n

    def pick_cups(self, n: int) -> Node[int]:
        return self.current.remove_next(n)

    def destination(self, picked: set[int]) -> Node[int]:
        for value in range(self.current.value - 1, 0, -1):  # O(N)
            if value not in picked:
                return self.values[value]
        n = self.current
        for k, v in self.values.items():  # O(N)
            if k > n.value and k not in picked:
                n = v
        return n

    @staticmethod
    def insert_cups(destination: Node[int], values: Node[int]) -> None:
        destination.append(values)

    def select_next(self) -> None:
        n = self.current.next
        if not n:
            raise ValueError("No next cup to select")
        self.current = n

    def move(self) -> None:
        picked = self.pick_cups(3)
        d = self.destination(set(picked))
        self.insert_cups(d, picked)
        self.select_next()

    def to_labels(self) -> str:
        labels = []
        node = self.current
        for _ in range(len(self.values)):
            labels.append(node.value)
            n = node.next
            if not n:
                raise ValueError("Inconsistent state of cups and their values")
            node = n
        first = labels.index(1)
        return "".join(str(x) for x in labels[first + 1 :] + labels[:first])


def play_crab_cups(cups: list[int]) -> str:
    circle = Circle(cups.copy())
    for _ in range(100):
        circle.move()
    return circle.to_labels()


def play_many_cups(cups: list[int]) -> int:
    cups = cups.copy()
    start = max(cups) + 1
    cups.extend(range(start, 1_000_000 + 1))
    circle = Circle(cups)
    for _ in range(10_000_000):
        circle.move()
    n1 = circle.values[1]
    n2 = n1.next
    assert n2
    n3 = n2.next
    assert n3
    return n2.value * n3.value


def parse_input(lines: list[str]) -> list[int]:
    return [int(x) for x in lines[0]]


def main() -> None:
    cups = parse_input(utils.read_input_lines(__file__))
    print(play_crab_cups(cups))
    print(play_many_cups(cups))


if __name__ == "__main__":
    main()
