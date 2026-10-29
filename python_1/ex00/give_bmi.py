def _is_number(value) -> bool:
    """Return True if value is an int or a float.

    bool is a subclass of int in Python, so True would pass an
    isinstance(value, int) test. We reject it on purpose: a BMI
    list is made of real numbers, not True / False.
    """
    if isinstance(value, bool):
        return False
    return isinstance(value, (int, float))


def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """Compute the BMI of each (height, weight) pair.

    BMI = weight / height^2.
    Height and weight must be two lists of the same length.
    On a bad input the error is printed and None is returned,
    so the program does not crash.
    """
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise AssertionError("height and weight must be lists")
        if len(height) != len(weight):
            raise AssertionError("the lists are not the same size")
        bmi_values = []
        for one_height, one_weight in zip(height, weight):
            if not _is_number(one_height) or not _is_number(one_weight):
                raise AssertionError("values must be int or float")
            if one_height <= 0:
                raise AssertionError("height must be greater than 0")
            if one_weight <= 0:
                raise AssertionError("weight must be greater than 0")
            bmi_values.append(one_weight / (one_height ** 2))
        return bmi_values
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
        return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return True where a BMI value is strictly above limit.

    "Above" means greater than the limit. A value equal to the
    limit stays False.
    """
    try:
        if not isinstance(bmi, list):
            raise AssertionError("bmi must be a list")
        if isinstance(limit, bool) or not isinstance(limit, int):
            raise AssertionError("limit must be an int")
        results = []
        for value in bmi:
            if not _is_number(value):
                raise AssertionError("bmi values must be int or float")
            results.append(value > limit)
        return results
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
        return None


def main() -> None:
    """Small demo used when this file is run directly."""
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except Exception as error:
        print(f"{type(error).__name__}: {error}")


if __name__ == "__main__":
    main()

