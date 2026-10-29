import matplotlib.pyplot as plt

from load_image import ft_load


def zoom_on_face(path: str) -> None:
    """Cut a square around the raccoon's face and show it.

    An image array is indexed as [row, column, channel].
    Row is the Y axis (top to bottom). Column is the X axis
    (left to right). Channel 0 is red, 1 is green, 2 is blue.
    """
    image = ft_load(path)
    if image is None:
        return
    # The tester of the subject also shows the original pixels.
    print(image)

    # 100:500 means "from row 100 up to, but not including, row 500".
    # That is 400 pixels. Same idea for the columns.
    # This window sits on the raccoon's face.
    square = image[100:500, 550:950]
    # :1 keeps a channel axis, so the shape is (400, 400, 1)
    # and not (400, 400). Both shapes are accepted by the subject.
    # We keep only the red channel. One channel is enough to draw grey.
    grey = square[:, :, :1]
    print(f"New shape after slicing: {grey.shape}")
    print(grey)

    # imshow draws the array. cmap="gray" maps low numbers to black
    # and high numbers to white. The ticks on the axes are the scale.
    plt.imshow(grey[:, :, 0], cmap="gray")
    plt.title("Zoom")
    plt.xlabel("X axis (pixels)")
    plt.ylabel("Y axis (pixels)")
    plt.show()


def main() -> None:
    """Load animal.jpeg, zoom, and display the result."""
    try:
        zoom_on_face("animal.jpeg")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
