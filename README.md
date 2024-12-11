# aoc_helper
A python package to automate the repetivite tasks in the advent of code.  

## Advent of Code Guidelines
This package does follow the automation guidelines on the [/r/adventofcode community wiki](https://www.reddit.com/r/adventofcode/wiki/faqs/automation.  
Specifically:
- This tools requests the Advent of Code server only to get the inputs once.
- The inputs are fetched once and then stored inside files.
- If you suspect one input is corrupted, you can manually delete it and it will be downloaded at the next execution of this day.
- The User-Agent header in [__download_and_get_input](/src/aoc_helper/utils.py#L30) is set to me since I maintain this tool.

## Presentation
This package allows you to automatically download the inputs and run the functions for the puzzle's part with a benchmark for the execution time.  
It might be able to run tests later if I take the time to implement it.  

**N.B.** this package won't submit the solutions for you, you still need to submit them manually.  

## Installation
Install from github:
```sh
pip install git+https://github.com/uAtomicBoolean/aoc_helper.git
```

Install from PyPi:
```sh
# Not available for the moment
```

## Use with multiple files
### Prepare the main file:  
Start by creating a `main.py` file in your project with the following code:
```python
import aoc_helper


# Which year you are trying to solve.
aoc_helper.set_year(2024)
# Where will you store your files for the days.
aoc_helper.set_days_folder("days")
# Your session cookie to download the puzzles' inputs.
aoc_helper.set_session_cookie("YOUR SESSION COOKIE")
```
To get your session cookie from the Advent of code:
- **Chrome/Brave** : press F12 and open the `Application` tab, then open the cookies for `adventofcode.com` and copy the value of `session`.  

### Solve the puzzles:  
Once this is done, you can create a file with any name in the days folder and use the following decorators to parse the input and solve the parts.
```python
import aoc_helper

# Register the function as the input's parser for day 1.
# It will download the input in an `inputs` folder if it isn't already done.
@aoc_helper.parser(1)
def input_parser(input: str):
	# Parse your input and return it.
	# Please note that any iterable needs to be encapsulated in a list to avoid an error.
	# So if you want to return a list of lines, you need to return it in a list to receive 
	# it correctly in your parts functions.
	return [input.splitlines()]


# Register the function as the first part solver for day 1.
@aoc_helper.part("one", 1)
def part_one(lines: list[str]):
	# Solve the part and return your result.
	return "result"


@aoc_helper.part("two", 1)
def part_two(lines: list[str]):
	# Solve the part and return your result.
	return "result"
```

### Run the solutions:  
Use the `aoc_helper run` command to run your solutions:
```sh
# Run all solutions.
aoc_helper run

# Run only one day.
aoc_helper run --day 1

# Specify what is the main file.
aoc_helper run aoc.py

# Or with one day
aoc_helper run aoc.py --day 1 
```

## Use with only one file
The only difference when using only one file is that you do not set the days folder.  
Otherwise, you use the same decorators.   

## Development
```sh
# Clone this repository
git clone https://github.com/uAtomicBoolean/aoc_helper.git

# Create a virtual environment
python3 -m venv venv && source venv/bin/activate

# Install the requirements.
pip install -r requirements.txt

# Install the package as editable.
pip install -e .
```  
You can now edit the package and test it in the `tests` folder.  
Some modifications might not be detected so you might need to re-install the package sometimes.  
