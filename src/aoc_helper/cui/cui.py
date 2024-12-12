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

        if day.part_one:
            bench, res = day.part_one()
            print(f"Part one: {res} ({bench:.4f}secs)")
        if day.part_two:
            bench, res = day.part_one()
            print(f"Part two: {res} ({bench:.4f}secs)")
        return

    sorted_days = dict(sorted(aoc_helper.DAYS.items()))
    for day, puzzle_data in sorted_days.items():
        if not puzzle_data.part_one and not puzzle_data.part_two:
            continue

        print("Running day", day)

        if puzzle_data.part_one:
            bench, res = puzzle_data.part_one()
            print(f"Part one: {res} ({bench:.4f}secs)")
        if puzzle_data.part_two:
            bench, res = puzzle_data.part_one()
            print(f"Part one: {res} ({bench:.4f}secs)")

        print()
