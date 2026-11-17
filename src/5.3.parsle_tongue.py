"""Module for extracting hidden secret messages from a binary image file."""

from collections.abc import Iterator

DEFAULT_FILE_PATH = "resources/logo.jpg"
CHUNK_SIZE = 1024
MIN_MESSAGE_LENGTH = 5
LOWER_A_ASCII = ord("a")
LOWER_Z_ASCII = ord("z")
EXCLAMATION_ASCII = ord("!")


def iter_file_chunks(
        file_path: str, chunk_size: int = CHUNK_SIZE
) -> Iterator[bytes]:
    """
    Yield chunks of bytes incrementally from a binary file.

    :param file_path: Path to the binary file
    :param chunk_size: Maximum number of bytes to read per chunk
    :return: Iterator yielding byte chunks
    """
    with open(file_path, "rb") as binary_file:
        while chunk := binary_file.read(chunk_size):
            yield chunk


def parsle_tongue(file_path: str = DEFAULT_FILE_PATH) -> list[str]:
    """
    Extract secret messages (5+ lowercase letters ending with '!') from
    a binary file.

    :param file_path: Path to the binary file to scan
    :return: List of extracted secret messages
    """
    secret_messages: list[str] = []
    current_letters: list[str] = []

    try:
        for chunk in iter_file_chunks(file_path):
            for byte_val in chunk:
                if LOWER_A_ASCII <= byte_val <= LOWER_Z_ASCII:
                    current_letters.append(chr(byte_val))
                elif byte_val == EXCLAMATION_ASCII:
                    if len(current_letters) >= MIN_MESSAGE_LENGTH:
                        secret_messages.append("".join(current_letters) + "!")
                    current_letters.clear()
                else:
                    current_letters.clear()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' was not found.")
        return []

    return secret_messages


def main() -> None:
    """Read resources/logo.jpg and print the extracted secret messages."""
    messages = parsle_tongue(DEFAULT_FILE_PATH)
    print(f"Found {len(messages)} secret messages: {messages}")


if __name__ == "__main__":
    main()
