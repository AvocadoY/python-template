"""Module for finding files with a specific prefix in a directory."""

from pathlib import Path

FILE_PREFIX = "deep"
IMAGES_DIR = "./images"
EXPECTED_COUNT = 2


def thats_the_way(dir_path: str) -> list[str]:
    """
    Finds all files in the specified directory whose names start with 'deep'.

    :param dir_path: Path to the directory to search in
    :return: List of matching filenames
    """
    target_dir = Path(dir_path)
    try:
        return [
            entry.name
            for entry in target_dir.iterdir()
            if entry.is_file() and entry.name.startswith(FILE_PREFIX)
        ]
    except (FileNotFoundError, NotADirectoryError):
        print(f"Error: Directory '{dir_path}' was not found.")
        return []


def main() -> None:
    """Verify that running thats_the_way on the images directory
    returns 2 files."""
    files_found = thats_the_way(IMAGES_DIR)
    if len(files_found) == EXPECTED_COUNT:
        print(f"returns {EXPECTED_COUNT} files: {files_found}")
    else:
        print(f"returns: {files_found}")


if __name__ == "__main__":
    main()
