#!/usr/bin/python3
"""
A simple script that demonstrates PEP 8 compliance.

This script calculates the factorial of a given number and prints the result.
"""

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    Args:
        n (int): The number for which the factorial is computed.

    Returns:
        int: The factorial of the number.

    Raises:
        ValueError: If n is a negative number.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def main():
    """
    Main function to run the script.

    Prompts the user for a number and prints its factorial.
    """
    try:
        number = int(input("Enter a non-negative integer: "))
        print(f"The factorial of {number} is {factorial(number)}.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
