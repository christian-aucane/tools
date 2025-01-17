from pathlib import Path

from utils import write_file


def generate_tree(path: Path) -> list:
    """
    Generate a nested list representing the directory tree structure, including the root folder.

    Args:
        path (Path): The root directory path.

    Returns:
        list: A nested list with directory and file names, starting with the root folder.
    """
    tree = [(path.absolute().name, [])]  # Include the root folder as the first element
    for p in path.iterdir():
        if p.is_dir():
            if p.name == "__pycache__":
                continue
            tree[0][1].append((p.name, generate_tree(p)))  # Recursively add subdirectories
        else:
            tree[0][1].append(p.name)  # Add file names
    return tree


def tree_to_str(tree: list, level: int = 0) -> str:
    """
    Convert the directory tree into a formatted string with indentation.

    Args:
        tree (list): The nested list representing the directory tree.
        level (int): The current indentation level.

    Returns:
        str: The formatted string representation of the directory tree.
    """
    string = ""
    for item in tree:
        string += '----' * level + f"| {item[0] if isinstance(item, tuple) else item}\n"
        if isinstance(item, tuple):  # If it's a directory, recursively call tree_to_str
            string += tree_to_str(item[1], level + 1)
    return string


def run(*args):
    """
    Entry point for the 'tree_to_txt' command.

    Args:
        args: The command arguments passed from the command line.
    """
    path = Path(args[0])  # Directory path
    output_path = Path(args[1])  # Output file path

    tree = generate_tree(path)  # Generate the directory tree
    tree_str = tree_to_str(tree)  # Convert the tree to a string
    write_file(tree_str, output_path)  # Save to the file

    print(f"The directory tree has been saved to {output_path}")


if __name__ == "__main__":
    run(".", "../outputs/tree.txt")