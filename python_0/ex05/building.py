import sys
import string

"""
ft_string_analysis.py

A command-line tool that analyzes a string and counts the occurrences
of uppercase letters, lowercase letters, digits, spaces, and punctuation marks.

Usage:
    python ft_string_analysis.py             # prompts user for input
    python ft_string_analysis.py "your text" # analyzes the provided argument

Raises:
    AssertionError: If more than one argument is passed via the command line.
"""


def print_counts(counts):
    """
    Prints the character analysis results in a formatted output.

    Args:
        counts (dict): A dictionary containing the following keys:
            - "len"         (int): Total number of characters in the string.
            - "uppercase"   (int): Number of uppercase letters.
            - "lowercase"   (int): Number of lowercase letters.
            - "punctuation" (int): Number of punctuation marks.
            - "spaces"      (int): Number of whitespace characters.
            - "digits"      (int): Number of numeric digits.

    Returns:
        None
    """
    print(f"The text contains {counts['len']} characters:")
    print(f"{counts['uppercase']} upper letters")
    print(f"{counts['lowercase']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")


def analyze_string(to_analyze):
    """
    Iterates over a string and counts each character category.

    Args:
        to_analyze (str): The input string to be analyzed.

    Returns:
        dict: A dictionary with the following keys and their counts:
            - "len"         (int): Total length of the string.
            - "uppercase"   (int): Count of uppercase letters (A-Z).
            - "lowercase"   (int): Count of lowercase letters (a-z).
            - "punctuation" (int): Count of punctuation marks.
            - "spaces"      (int): Count of whitespace characters.
            - "digits"      (int): Count of numeric digits (0-9).
    """
    counts = {
        "len": len(to_analyze),
        "uppercase": 0,
        "lowercase": 0,
        "punctuation": 0,
        "spaces": 0,
        "digits": 0
    }
    for char in to_analyze:
        if char.isupper():
            counts["uppercase"] += 1
        elif char.islower():
            counts["lowercase"] += 1
        elif char.isdigit():
            counts["digits"] += 1
        elif char.isspace():
            counts["spaces"] += 1
        elif char in string.punctuation:
            counts["punctuation"] += 1
    return counts


def main(object):

    if len(object) > 2:
        raise AssertionError("more than one argument is provided")
    if len(object) == 1:
        name = input("What is the text to count?: ")
        print_counts(analyze_string(name))
        return
    print_counts(analyze_string(object[1]))


if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(f"AssertionError: {e}")
