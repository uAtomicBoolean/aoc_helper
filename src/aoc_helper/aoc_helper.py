import sys
import time
import datetime
from collections.abc import Iterable
from .utils import __download_and_get_input
from .types import Puzzle


DAYS: dict[int, Puzzle] = {}
SESSION_COOKIE = None
YEAR: int = None
DAYS_FOLDER: str = None


def set_year(year: int):
    global YEAR

    current_year = datetime.date.today().year
    if year < 2015 or year > current_year:
        print(f"You can't define a year superior to {current_year}.", file=sys.stderr)
        sys.exit(1)

    YEAR = year


def set_days_folder(folder: str):
    global DAYS_FOLDER

    if not folder:
        print("You must pass a valid path (ex: 'days').", file=sys.stderr)
        sys.exit(1)

    DAYS_FOLDER = folder


def set_session_cookie(cookie: str):
    global SESSION_COOKIE

    if not cookie:
        raise ValueError("Cookie must not be empty.")
    SESSION_COOKIE = cookie


def parser(day: int):
    """Register a function as a day's input parser.

    The day's input will be downloaded and saved in a file on the first execute.
    This avoid downloading the input at each execution.

    Args:
        day (int): the day linked to the parser.

    Raises:
        ValueError: error raised if the day passed as a parameter is not in the following range [1, 25].
    """

    if day < 1 or day > 25:
        raise ValueError("'day' must be between 1 and 25 (both included).")

    def wrapper(func):
        def new_func():
            if not YEAR:
                print("You must set the year of the calendar.", file=sys.stderr)
                sys.exit(1)

            if not SESSION_COOKIE:
                print(
                    "Please, set your session cookie at the start of the code.",
                    file=sys.stderr,
                )
                sys.exit(1)

            day_input = __download_and_get_input(YEAR, day, SESSION_COOKIE)
            return func(day_input)

        curr_day: Puzzle = DAYS.get(day, Puzzle())
        curr_day.parse_input = new_func
        DAYS[day] = curr_day

        return new_func

    return wrapper


def part(part: str, day: int):
    """Register a function as a puzzle's part.

    A part can either use the input parsed from the `parser` decorated function, or
    use a manually passed input.

    ```
    @parser
    def parse_input(raw_input: str)
        # parse input
        return raw_input

    @part("one", 1)
    def part_one(puzzle_input: str):
        print(puzzle_input)

    # Call with the parsed input
    part_one()

    # Call with manual input
    part_one("This is my input")
    ```

    Args:
        part (str): the part solved by the function.
        day (int): the day solved by the function.

    Raises:
        ValueError: raised if 'part' or 'day' are not following the requirements.
    """

    if part not in ["one", "two"]:
        raise ValueError("'part' Argument must be one of : one, two.")

    if day < 1 or day > 25:
        raise ValueError("'day' must be between 1 and 25 (both included).")

    def wrapper(func):
        def new_func(*args):
            if args:
                return func(*args)

            curr_day: Puzzle = DAYS.get(day, Puzzle())
            if not curr_day.parse_input:
                print(f"Missing parser for day {day} part {part}", file=sys.stderr)
                sys.exit(1)

            day_input = curr_day.parse_input()

            start = time.perf_counter()
            if isinstance(day_input, Iterable):
                res = func(*day_input)
            else:
                res = func(day_input)
            return time.perf_counter() - start, res

        curr_day: Puzzle = DAYS.get(day, Puzzle())

        if part == "one":
            curr_day.part_one = new_func
        elif part == "two":
            curr_day.part_two = new_func

        DAYS[day] = curr_day

        return new_func

    return wrapper
