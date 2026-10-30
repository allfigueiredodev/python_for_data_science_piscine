import io

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from load_image import ft_load

RED = 0
GREEN = 1
BLUE = 2
CHANNEL_AXIS = 2
OFF = 0


def _check_image(array) -> None:
    """Reject a missing image or one that has no color channels."""
    if array is None or not hasattr(array, "ndim") or array.ndim != 3:
        raise AssertionError("array must be an RGB image")
    if array.shape[CHANNEL_AXIS] < 3:
        raise AssertionError("array must have red, green and blue channels")


def _display(image, title: str) -> None:
    """Show the image with its title.

    The figure is drawn by Matplotlib, then opened with PIL,
    because plt.show() cannot open a window here.
    """
    plt.imshow(image)
    plt.title(title)
    plt.axis("off")
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", bbox_inches="tight")
    plt.close()
    buffer.seek(0)
    Image.open(buffer).show()


def ft_invert(array):
    """Inverts the color of the image received."""
    try:
        _check_image(array)
        limit = int(np.iinfo(array.dtype).max)
        inverted = limit - array
        _display(inverted, "Invert")
        return inverted
    except Exception as error:
        print(f"Error: {error}")
        return None


def ft_red(array):
    """Keep only the red channel of the image."""
    try:
        _check_image(array)
        red_image = array.copy()
        red_image[:, :, GREEN] = red_image[:, :, GREEN] * OFF
        red_image[:, :, BLUE] = red_image[:, :, BLUE] * OFF
        _display(red_image, "Red")
        return red_image
    except Exception as error:
        print(f"Error: {error}")
        return None


def ft_green(array):
    """Keep only the green channel of the image."""
    try:
        _check_image(array)
        green_image = array.copy()
        green_image[:, :, RED] = green_image[:, :, RED] - green_image[:, :, RED]
        green_image[:, :, BLUE] = green_image[:, :, BLUE] - green_image[:, :, BLUE]
        _display(green_image, "Green")
        return green_image
    except Exception as error:
        print(f"Error: {error}")
        return None


def ft_blue(array):
    """Keep only the blue channel of the image."""
    try:
        _check_image(array)
        blue_image = array.copy()
        blue_image[:, :, RED] = OFF
        blue_image[:, :, GREEN] = OFF
        _display(blue_image, "Blue")
        return blue_image
    except Exception as error:
        print(f"Error: {error}")
        return None


def ft_grey(array):
    """Turn the image into shades of grey."""
    try:
        _check_image(array)
        grey_image = array.copy()
        channel_count = array.shape[CHANNEL_AXIS]
        average = array.sum(axis=CHANNEL_AXIS, dtype=int) / channel_count
        grey_image[:, :, RED] = average
        grey_image[:, :, GREEN] = average
        grey_image[:, :, BLUE] = average
        _display(grey_image, "Grey")
        return grey_image
    except Exception as error:
        print(f"Error: {error}")
        return None


def main() -> None:
    """Apply every filter to the landscape image."""
    try:
        array = ft_load("landscape.jpg")
        if array is None:
            return
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)
        print(ft_invert.__doc__)
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
