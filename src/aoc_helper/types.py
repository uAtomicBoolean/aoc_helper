from typing import Callable
from dataclasses import dataclass


@dataclass
class Puzzle:
    parse_input: Callable = None
    part_one: Callable = None
    part_two: Callable = None
