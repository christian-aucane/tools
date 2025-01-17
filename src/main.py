"""
This is the main script.

It parses arguments and calls the appropriate script based on the command.
"""
from argparse import ArgumentParser
import importlib


def parse_args():
    """Parse the command-line arguments."""
    parser = ArgumentParser(description="Command-line utility to execute various tasks.")
    parser.add_argument("command", type=str, help="The command to execute (e.g., 'tree_to_txt')")
    parser.add_argument("args", nargs='*', help="The arguments to pass to the specified command.")

    args = parser.parse_args()
    return args


def main():
    """Main function to handle argument parsing and execute the appropriate command."""
    args = parse_args()

    try:
        # Dynamically import the module corresponding to the command
        module = importlib.import_module(args.command)

        # Check if the 'run' function exists in the module
        if hasattr(module, 'run'):
            # Get the 'run' function from the module
            run_func = getattr(module, 'run')

            # Pass all arguments to the 'run' function
            run_func(*args.args)
        else:
            raise ValueError(f"No 'run' function found in the module {args.command}")

    except ModuleNotFoundError:
        print(f"The module {args.command} does not exist.")
    except Exception as e:
        print(f"Error while executing the command {args.command}: {e}")


if __name__ == "__main__":
    main()
