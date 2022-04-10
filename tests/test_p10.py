from aoc20.p10 import count_combinations, parse_input, sort_adapters


def test_example():
    data = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
""".strip().splitlines()
    assert sort_adapters(parse_input(data)) == 22 * 10


def test_combinations_1():
    data = """
16
10
15
5
1
11
7
19
6
12
4
""".strip().splitlines()
    assert count_combinations(parse_input(data)) == 8


def test_combinations_2():
    data = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
""".strip().splitlines()
    assert count_combinations(parse_input(data)) == 19208
