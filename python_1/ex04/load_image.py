import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Load a JPG or JPEG image and print its shape.

    The array shape is (height, width, 3).
    The 3 channels are red, green, then blue.
    On failure the error is printed and None is returned.
    """
    try:
        if not isinstance(path, str):
            raise AssertionError("path must be a string")
        lower_path = path.lower()
        is_jpeg = lower_path.endswith(".jpg") or lower_path.endswith(".jpeg")
        if not is_jpeg:
            raise AssertionError("only JPG and JPEG files are supported")
        # "with" closes the file even if something fails inside the block.
        with Image.open(path) as image:
            # convert("RGB") forces 3 channels, even for a grey file.
            pixels = np.array(image.convert("RGB"))
        print(f"The shape of image is: {pixels.shape}")
        return pixels
    except Exception as error:
        print(f"Error: {error}")
        return None


def main() -> None:
    """Load the sample landscape when this file is run directly."""
    try:
        image = ft_load("landscape.jpg")
        print(image)
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
