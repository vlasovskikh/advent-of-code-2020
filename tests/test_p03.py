from aoc20.p03 import parse_input, count_trees, check_slopes


def test_example():
    data = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".strip().splitlines()
    assert count_trees(parse_input(data), 3, 1) == 7


def test_check_slopes():
    data = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".strip().splitlines()
    assert (
        check_slopes(
            parse_input(data),
            [
                (1, 1),
                (3, 1),
                (5, 1),
                (7, 1),
                (1, 2),
            ],
        )
        == 336
    )
