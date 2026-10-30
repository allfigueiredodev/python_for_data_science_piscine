import io

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from load_image import ft_load


def transpose_image(image: np.ndarray) -> np.ndarray:
    """Swap rows and columns with two loops.

    The rule is: new[column][row] = old[row][column].
    After the swap, what used to be a column is a row.
    A library transpose (.T or np.transpose) is not used.
    """
    if image.ndim == 3:
        table = image[:, :, 0]
    else:
        table = image
    height, width = table.shape
    turned = []
    for column in range(width):
        new_row = []
        for row in range(height):
            new_row.append(int(table[row][column]))
        turned.append(new_row)
    return np.array(turned)


def rotate(
    path: str,
    start_y: int,
    start_x: int,
    height: int,
    width: int,
    channel: int,
) -> None:
    """Crop a rectangle, transpose it, and display the result.

    start_y / start_x: top-left corner of the crop.
    height / width: size of the crop in pixels.
    channel: which color to keep (0 = red, 1 = green, 2 = blue).
    """
    try:
        if not isinstance(path, str):
            raise AssertionError("path must be a string")
        for name, value in (
            ("start_y", start_y),
            ("start_x", start_x),
            ("height", height),
            ("width", width),
            ("channel", channel),
        ):
            if isinstance(value, bool) or not isinstance(value, int):
                raise AssertionError(f"{name} must be an int")
        if height <= 0 or width <= 0:
            raise AssertionError("height and width must be greater than 0")
        if channel < 0 or channel > 2:
            raise AssertionError("channel must be 0, 1 or 2")

        image = ft_load(path)
        if image is None:
            return

        end_y = start_y + height
        end_x = start_x + width
        if start_y < 0 or start_x < 0 or end_y > image.shape[0] or end_x > image.shape[1]:
            raise AssertionError("crop window is outside the image")

        square = image[start_y:end_y, start_x:end_x, channel:channel + 1]
        print(f"The shape of image is: {square.shape} or {square.shape[:2]}")
        print(square)

        turned = transpose_image(square)
        print(f"New shape after Transpose: {turned.shape}")
        print(turned)

        plt.imshow(turned, cmap="gray")
        buffer = io.BytesIO()
        plt.savefig(buffer, format="png", bbox_inches="tight")
        plt.close()
        buffer.seek(0)
        Image.open(buffer).show()
    except Exception as error:
        print(f"Error: {error}")


def main() -> None:
    """Example: crop the same face window as zoom.py, then transpose it."""
    try:
        rotate("animal.jpeg", 100, 550, 400, 400, 0)
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
