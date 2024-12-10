import aoc_helper


@aoc_helper.parser(1)
def parse_input(raw_input: str):
    lines = raw_input.split("\n")
    left, right = [], []
    for l in lines:
        left.append(l.split()[0])
        right.append(l.split()[1])
    return left, right


@aoc_helper.part("one", 1)
def part_one(left: list[str], right: list[str]):
    return 1


def test_part_one():
    assert part_one() == 4


def test_part_two():
    assert part_one() == 4
