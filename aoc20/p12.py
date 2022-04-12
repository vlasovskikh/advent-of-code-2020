from aoc20 import utils


def follow_instructions(instructions: list[tuple[str, int]]) -> int:
    north, east, face = 0, 0, 0
    for cmd, arg in instructions:
        if cmd == "N":
            north += arg
        elif cmd == "S":
            north -= arg
        elif cmd == "E":
            east += arg
        elif cmd == "W":
            east -= arg
        elif cmd == "L":
            face -= arg
            face %= 360
        elif cmd == "R":
            face += arg
            face %= 360
        elif cmd == "F":
            if face == 0:
                east += arg
            elif face == 90:
                north -= arg
            elif face == 180:
                east -= arg
            elif face == 270:
                north += arg
            else:
                raise ValueError(f"Unknown face direction: {face}")
        else:
            raise ValueError(f"Unknown command: {cmd}")
    return abs(east) + abs(north)


def follow_waypoint(instructions: list[tuple[str, int]]) -> int:
    ship_east, ship_north = 0, 0
    waypoint_east, waypoint_north = 10, 1
    for cmd, arg in instructions:
        if cmd == "N":
            waypoint_north += arg
        elif cmd == "S":
            waypoint_north -= arg
        elif cmd == "E":
            waypoint_east += arg
        elif cmd == "W":
            waypoint_east -= arg
        elif cmd in ("L", "R"):
            if cmd == "L":
                arg = 360 - arg
            arg %= 360
            if arg == 0:
                pass
            elif arg == 90:
                waypoint_east, waypoint_north = waypoint_north, -waypoint_east
            elif arg == 180:
                waypoint_east, waypoint_north = -waypoint_east, -waypoint_north
            elif arg == 270:
                waypoint_east, waypoint_north = -waypoint_north, waypoint_east
            else:
                raise ValueError(f"Unknown angle: {arg}")
        elif cmd == "F":
            ship_east += waypoint_east * arg
            ship_north += waypoint_north * arg
        else:
            raise ValueError(f"Unknown command: {cmd}")
    return abs(ship_east) + abs(ship_north)


def parse_input(lines: list[str]) -> list[tuple[str, int]]:
    result: list[tuple[str, int]] = []
    for line in lines:
        cmd, arg = line[0], line[1:]
        result.append((cmd, int(arg)))
    return result


def main() -> None:
    instructions = parse_input(utils.read_input_lines(__file__))
    print(follow_instructions(instructions))
    print(follow_waypoint(instructions))


if __name__ == "__main__":
    main()
