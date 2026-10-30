def _is_number(value) -> bool:
    """Return True for int and float, False for bool.

    See give_bmi.py: bool is a subclass of int, so it needs its own test.
    """
    if isinstance(value, bool):
        return False
    return isinstance(value, (int, float))


def slice_me(family: list, start: int, end: int) -> list:
    """Print the shape of a 2D list, then return family[start:end].

    Shape is (number of rows, number of columns).
    Slicing is the same tool you use on a string or a list:
    the start index is kept, the end index is left out.
    A negative end counts from the back of the list.
    """
    try:
        if not isinstance(family, list) or len(family) == 0:
            raise AssertionError("family must be a non-empty 2D list")
        if isinstance(start, bool) or not isinstance(start, int):
            raise AssertionError("start must be an int")
        if isinstance(end, bool) or not isinstance(end, int):
            raise AssertionError("end must be an int")

        width = len(family[0])
        for row in family:
            if not isinstance(row, list) or len(row) != width:
                raise AssertionError("family must be a rectangle of numbers")
            for value in row:
                if not _is_number(value):
                    raise AssertionError("values must be int or float")

        print(f"My shape is : ({len(family)}, {width})")
        sliced = [row[:] for row in family[start:end]]
        new_width = len(sliced[0]) if sliced else 0
        print(f"My new shape is : ({len(sliced)}, {new_width})")
        return sliced
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
        return None


def main() -> None:
    """Run the example from the subject."""
    try:
        family = [
            [1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2],
        ]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except Exception as error:
        print(f"{type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
