import matplotlib.pyplot as plt

from load_image import ft_load


def _display(image, title: str) -> None:
    """Open a window so we can see the filter."""
    plt.imshow(image)
    plt.title(title)
    plt.xlabel("X axis (pixels)")
    plt.ylabel("Y axis (pixels)")
    plt.show()


def ft_invert(array):
    """Inverts the color of the image received."""
    # Each channel is a number from 0 to 255.
    # 255 minus that number flips the color: black becomes white.
    # A copy is made by the subtraction, so the original stays intact.
    # Allowed operators here: =, +, -, *
    inverted = 255 - array
    _display(inverted, "Invert")
    return inverted


def ft_red(array):
    """Keep only the red channel of the image."""
    # Allowed operators here: =, *
    # Multiplying green and blue by 0 turns those channels off.
    red_image = array.copy()
    red_image[:, :, 1] = red_image[:, :, 1] * 0
    red_image[:, :, 2] = red_image[:, :, 2] * 0
    _display(red_image, "Red")
    return red_image


def ft_green(array):
    """Keep only the green channel of the image."""
    # Allowed operators here: =, -
    # A channel minus itself is 0, so red and blue disappear.
    green_image = array.copy()
    green_image[:, :, 0] = green_image[:, :, 0] - green_image[:, :, 0]
    green_image[:, :, 2] = green_image[:, :, 2] - green_image[:, :, 2]
    _display(green_image, "Green")
    return green_image


def ft_blue(array):
    """Keep only the blue channel of the image."""
    # Allowed operator here: =
    # We can only assign. 0 assigned to a channel clears it.
    blue_image = array.copy()
    blue_image[:, :, 0] = 0
    blue_image[:, :, 1] = 0
    _display(blue_image, "Blue")
    return blue_image


def ft_grey(array):
    """Turn the image into shades of grey."""
    # Allowed operators here: =, /
    # sum() is a method, not the + operator, so the rule still holds.
    # Dividing the total of the 3 channels by 3 is their average.
    # dtype=int avoids overflow: a color channel only holds 0 to 255.
    grey_image = array.copy()
    average = array.sum(axis=2, dtype=int) / 3
    grey_image[:, :, 0] = average
    grey_image[:, :, 1] = average
    grey_image[:, :, 2] = average
    _display(grey_image, "Grey")
    return grey_image


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
