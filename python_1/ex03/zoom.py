import io

import matplotlib.pyplot as plt
from PIL import Image

from load_image import ft_load


def zoom(
    path: str,
    start_y: int,
    start_x: int,
    height: int,
    width: int,
    channel: int,
) -> None:
    """Load an image, zoom to a region, keep one color channel, and show it.

    start_y / start_x: top-left corner of the zoom window.
    height / width: size of the zoom window in pixels.
    channel: which color to keep (0 = red, 1 = green, 2 = blue).

    An image array is indexed as [row, column, channel].
    Row is the Y axis (top to bottom). Column is the X axis
    (left to right).
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
        print(image)

        end_y = start_y + height
        end_x = start_x + width
        if start_y < 0 or start_x < 0 or end_y > image.shape[0] or end_x > image.shape[1]:
            raise AssertionError("zoom window is outside the image")

        zoomed = image[start_y:end_y, start_x:end_x, channel:channel + 1]
        print(f"New shape after slicing: {zoomed.shape} or {zoomed.shape[:2]}")
        print(zoomed)

        plt.imshow(zoomed[:, :, 0], cmap="gray")
        buffer = io.BytesIO()
        plt.savefig(buffer, format="png", bbox_inches="tight")
        plt.close()
        buffer.seek(0)
        Image.open(buffer).show()
    except Exception as error:
        print(f"Error: {error}")


def main() -> None:
    """Example call: zoom on the raccoon's face, keep the red channel."""
    try:
        zoom("animal.jpeg", 100, 550, 400, 400, 0)
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
