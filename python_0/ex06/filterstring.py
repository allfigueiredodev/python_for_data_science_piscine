import sys
from ft_filter import ft_filter


def main(args):
    if len(args) != 3:
        raise AssertionError("the arguments are bad")

    try:
        string = str(args[1])
        number = int(args[2])
        if not isinstance(args[1], str) or not isinstance(number, int):
            raise AssertionError("the arguments are bad")
    except ValueError:
        raise AssertionError("the arguments are bad")

    words = string.split(" ")
    result = ft_filter(lambda word: len(word) > number, words)
    print(result)


if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(f"AssertionError: {e}")
