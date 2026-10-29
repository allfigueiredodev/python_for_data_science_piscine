import numpy as np
import matplotlib.pyplot as plt

from load_image import ft_load


def cut_square(image: np.ndarray) -> np.ndarray:
    """Return a 400x400 grey square around the raccoon's face.

    Same window as in zoom.py, so the two exercises show the same crop.
    The result keeps one channel: shape (400, 400, 1).
    """
    square = image[100:500, 550:950]
    return square[:, :, :1]


def transpose_image(image: np.ndarray) -> np.ndarray:
    """Swap rows and columns with two loops.

    The subject forbids a library transpose (no .T, no np.transpose).
    The rule is: new[column][row] = old[row][column].
    After the swap, what used to be a column is a row.
    """
    # Read the single channel as a plain 2D table of numbers.
    if image.ndim == 3:
        table = image[:, :, 0]
    else:
        table = image
    height, width = table.shape
    turned = []
    for column in range(width):
        new_row = []
        for row in range(height):
            # int() so the printed values stay whole numbers.
            new_row.append(int(table[row][column]))
        turned.append(new_row)
    return np.array(turned)


def main() -> None:
    """Load the animal, cut a square, transpose it, and display it."""
    try:
        image = ft_load("animal.jpeg")
        if image is None:
            return
        square = cut_square(image)
        print(f"The shape of image is: {square.shape}")
        print(square)
        turned = transpose_image(square)
        print(f"New shape after Transpose: {turned.shape}")
        print(turned)
        plt.imshow(turned, cmap="gray")
        plt.title("Transpose")
        plt.xlabel("X axis (pixels)")
        plt.ylabel("Y axis (pixels)")
        plt.show()
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
