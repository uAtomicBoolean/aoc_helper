import aoc_helper


@aoc_helper.parser(2)
def parse_input(raw_input: str):
    return tuple(raw_input.splitlines())


@aoc_helper.part("one", 2)
def part_one(lines: list[str]):
    print(lines)
    return 2


def test_part_one():
    assert part_one() == 4


def test_part_two():
    assert part_one() == 4
