import sys
import pathlib
import importlib
import importlib.util


def __get_day_argument(args: list[str]):
    if "--day" not in args:
        return False

    arg_index = args.index("--day")
    if arg_index == len(args) - 1:
        print("Missing value for argument '--day'.", file=sys.stderr)
        sys.exit(1)

    value_index = arg_index + 1
    try:
        day_value = int(args[value_index])
        cast_error = False
    except ValueError:
        cast_error = True

    if cast_error or day_value < 1 or day_value > 25:
        print(
            "Value of argument '--day' must be an integer between 1 and 25 included.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Cleaning the args list to ease the interpretation of remaining arguments.
    args.remove("--day")
    args.remove(str(day_value))

    if len(args) > 1:
        print("Too many arguments.", file=sys.stderr)
        sys.exit(1)

    return day_value


def __find_main_file(args: list[str]):
    if len(args):
        if args[0].endswith(".py"):
            main_file = pathlib.Path(args[0])
            if main_file.exists():
                return __load_main_file(main_file)

        print("Couldn't find the following main file:", args[0], file=sys.stderr)
        sys.exit(1)

    for file in ["main.py", "test_main.py"]:
        main_file = pathlib.Path(file)
        if main_file.exists():
            return __load_main_file(main_file)

    print(
        "Couldn't find a default main file, please specify a path when running the command.",
        file=sys.stderr,
    )
    sys.exit(1)


def __load_main_file(main_file: pathlib.Path):
    main_spec = importlib.util.spec_from_file_location("main", main_file)
    main_module = importlib.util.module_from_spec(main_spec)
    main_spec.loader.exec_module(main_module)

    # TODO Discover all the files linked to the days.
    # TODO Tell the user to save his days files in the folder 'days'.
    # TODO Other options, add a function to load the days. This function would be called from the
    #   main file and would take the path to the days folder.
