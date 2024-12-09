import os
import sys
import pathlib
import requests


def __download_and_get_input(day: int, SESSION_COOKIE: str):
    """Download the input for the given day.

    Args:
        day (int): the day to download the input from.

    Raises:
        RuntimeError: _description_

    Returns:
        str: The downloaded input
    """

    inputs_path = pathlib.Path().joinpath("inputs").resolve()
    if not inputs_path.exists():
        os.mkdir(inputs_path)

    file_path = inputs_path.joinpath(f"day{day}.txt").resolve()

    if not file_path.exists():
        with requests.get(
            f"https://adventofcode.com/2024/day/{day}/input",
            cookies={"session": SESSION_COOKIE},
        ) as req:
            if req.status_code == 400:
                print(
                    "An error occured while trying to get the puzzle's input. "
                    "Please check that your cookie is fine.",
                    file=sys.stderr,
                )
                sys.exit(1)

            if req.status_code != 200:
                req.raise_for_status()

            with open(file_path, "w") as file:
                file.write(req.content.decode(encoding="utf-8").strip())

    return file_path.read_text()
