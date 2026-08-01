"""
Generation logic for Iranian National Codes.

Two generators are provided:

- generate(): produces a random, checksum-valid 10-digit code where
  each of the first 9 digits is drawn uniformly from 0-9.
- generate_round(): produces a random, checksum-valid 10-digit code
  using a shrinking upper bound for each digit, which tends to
  produce "rounder" looking codes (more repeated low digits).
"""

import random


def _checksum(digits) -> int:
    """Compute the checksum digit for the first 9 digits."""
    weighted_sum = sum(d * (10 - i) for i, d in enumerate(digits))
    remainder = weighted_sum % 11
    return remainder if remainder < 2 else 11 - remainder


def generate() -> str:
    """
    Generate a random, valid Iranian National Code.

    Each of the first 9 digits is chosen uniformly at random from
    0-9, and the 10th digit is the computed checksum.

    Returns:
        A 10-character string representing a valid national code.

    Example:
        >>> code = generate()
        >>> len(code)
        10
    """
    digits = [random.randint(0, 9) for _ in range(9)]
    digits.append(_checksum(digits))
    return "".join(str(d) for d in digits)


def generate_round() -> str:
    """
    Generate a random, valid Iranian National Code with a "rounder"
    digit pattern (a shrinking random upper bound is used for each
    successive digit, so lower digits become more likely as the code
    is built).

    The result is guaranteed not to have all 10 digits identical.

    Returns:
        A 10-character string representing a valid national code.
    """
    digits = []
    upper_bound = 10

    for _ in range(9):
        upper_bound = max(upper_bound, 2) if upper_bound < 2 else upper_bound
        digit = random.randint(0, upper_bound - 1)
        digits.append(digit)
        upper_bound = digit

    digits.append(_checksum(digits))

    if len(set(digits)) == 1:
        return generate_round()

    return "".join(str(d) for d in digits)
