import os
import aoc_helper


aoc_helper.set_year(2024)
aoc_helper.set_session_cookie(os.getenv("SESSION_COOKIE"))


@aoc_helper.parser(2)
def parse_input(raw_input: str):
    lines = raw_input.split("\n")
    left, right = [], []
    for l in lines:
        left.append(l.split()[0])
        right.append(l.split()[1])
    return left, right


@aoc_helper.part("one", 2)
def part_one(left: list[str], right: list[str]):
    return 4


def test_part_one():
    assert part_one() == 4


def test_part_two():
    assert part_one() == 4


part_one()
