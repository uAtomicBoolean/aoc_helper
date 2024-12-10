import sys
from typing import Union

from . import utils
from .. import aoc_helper


def main():
    args = sys.argv[1:]
    if not len(args):
        print("You must use one of the following command: run, test.")

    command = args[0]
    args = args[1:]

    targeted_day = utils.__get_day_argument(args)
    utils.__find_main_file(args)

    if command == "run":
        return run_command(targeted_day)
    elif command == "test":
        return test_command(targeted_day)

    print(
        "No command found, please specify a command to run: run, test.", file=sys.stderr
    )
    sys.exit(1)


def run_command(targeted_day: Union[int, bool] = False):

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

    sorted_days = dict(sorted(aoc_helper.DAYS.items()))
    for day, puzzle_data in sorted_days.items():
        if not puzzle_data.part_one and not puzzle_data.part_two:
            continue

        # TODO Beautify the display.
        print("Running day", day)

        if puzzle_data.part_one:
            print("\tPart one:", puzzle_data.part_one())
        if puzzle_data.part_two:
            print("\tPart two:", puzzle_data.part_two())
        print()


def test_command(targeted_day: Union[int, bool] = False):
    print(targeted_day)

    # TODO
