
from pathlib import Path



def write_file(string: str, path: Path):
    with open(path, "w") as f:
        f.write(string)
