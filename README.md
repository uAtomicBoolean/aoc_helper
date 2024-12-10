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
Explain the functionnalities: auto-downloading the inputs, benchmarking the functions, running all days or only one, running tests.  

## Installation
TODO  

## How to use
Explain the settings.  
Explain the decorators.  
Explain the catch with the @parser() decorator (the fact that iterables needs to be encapsulated in a list to avoid being deconstructed).  
Explain that it can be used either with multiple days files or with only one file (set_days_folder necessary for multiple files).

## Development
TODO 