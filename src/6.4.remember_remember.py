"""Module for decoding hidden messages stored as black pixels in an image."""

from PIL import Image

DEFAULT_IMAGE_PATH = "resources/code.png"
BLACK_PIXEL = (0, 0, 0)


def remember_remember(image_path: str = DEFAULT_IMAGE_PATH) -> str:
    """
    Decode a hidden message from an image where each column has one black
    pixel.

    :param image_path: Path to the encoded image file
    :return: The decoded secret message
    """
    try:
        with Image.open(image_path) as raw_image:
            image = raw_image.convert("RGB")
            width, height = image.size
            decoded_chars = [
                chr(row)
                for col in range(width)
                for row in range(height)
                if image.getpixel((col, row)) == BLACK_PIXEL
            ]
        return "".join(decoded_chars)
    except FileNotFoundError:
        print(f"Error: Image file '{image_path}' was not found.")
        return ""


def main() -> None:
    """Decode and print the secret message from the default image."""
    secret_message = remember_remember(DEFAULT_IMAGE_PATH)
    print(f"Decoded message: {secret_message}")


if __name__ == "__main__":
    main()
