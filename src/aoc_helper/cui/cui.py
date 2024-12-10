import sys
from . import utils
from .. import aoc_helper


def main():
    args = sys.argv[1:]
    if not len(args):
        print("You must use one of the following command: run, test.")

    if args[0] == "run":
        return run_command(args[1:])
    elif args[0] == "test":
        return test_command(args[1:])

    print(
        "No command found, please specify a command to run: run, test.", file=sys.stderr
    )
    sys.exit(1)


def run_command(args: list[str]):
    targeted_day = utils.__get_day_argument(args)
    utils.__find_main_file(args)

    if targeted_day:
        if targeted_day not in aoc_helper.DAYS:
            print("No functions were defined for the targeted day.", file=sys.stderr)
            sys.exit(1)

        day = aoc_helper.DAYS[targeted_day]
        if not day.part_one and not day.part_two:
            print(
                "No functions defined as puzzle parts for the targeted day.",
                file=sys.stderr,
            )
            sys.exit(1)

        # TODO Add benchmarking
        if day.part_one:
            print("Part one:", day.part_one())
        if day.part_two:
            print("Part two:", day.part_two())
        return

    for day, puzzle_data in aoc_helper.DAYS.items():
        if not puzzle_data.part_one and not puzzle_data.part_two:
            continue

        # TODO Beautify the display.
        print("###################################")
        print("Running day", day)
        print("###################################")

        if puzzle_data.part_one:
            print("Part one:", puzzle_data.part_one())
        if puzzle_data.part_two:
            print("Part two:", puzzle_data.part_two())


def test_command(args: list[str]):
    day_arg = utils.__get_day_argument(args)
    utils.__find_main_file(args)

    # TODO
