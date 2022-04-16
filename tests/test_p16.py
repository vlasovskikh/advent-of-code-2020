from aoc20.p16 import parse_input, nearby_error_rate, restore_your_ticket


def test_example():
    data = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
""".strip().splitlines()
    assert nearby_error_rate(parse_input(data)) == 71


def test_departure():
    data = """
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
""".strip().splitlines()
    assert restore_your_ticket(parse_input(data)) == {
        "class": 12,
        "row": 11,
        "seat": 13,
    }
