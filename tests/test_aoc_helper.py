import aoc_helper

aoc_helper.set_session_cookie("YOUR COOKIE")


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
    print(len(left), len(right))


part_one()
part_one([1, 2, 3], [4, 5, 6])
