import aoc_helper


@aoc_helper.parser(2)
def parse_input(raw_input: str):
    return [raw_input.splitlines()]


@aoc_helper.part("one", 2)
def part_one(lines: list[str]):
    return 2.1


@aoc_helper.part("two", 2)
def part_two(lines: list[str]):
    return 2.2


def test_part_one():
    assert part_one() == 4


def test_part_two():
    assert part_one() == 4
