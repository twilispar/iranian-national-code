"""
Validation logic for Iranian National Codes.

An Iranian National Code is a 10-digit string. The last digit is a
checksum computed from the first 9 digits using weighted sums modulo 11.
"""

import re
from typing import List, Sequence

_CODE_PATTERN = re.compile(r"^[0-9]{10}$")

_ALL_DIGITS_EQUAL = {str(d) * 10 for d in range(10)}


def validate(code: str) -> bool:
    """
    Validate a single Iranian National Code.

    Args:
        code: A 10-digit string representing the national code.

    Returns:
        True if the code is a syntactically and checksum-valid
        Iranian National Code, False otherwise.

    Example:
        >>> validate("0499370899")
        True
        >>> validate("1111111111")
        False
    """
    if not isinstance(code, str):
        return False

    if code in _ALL_DIGITS_EQUAL or not _CODE_PATTERN.match(code):
        return False

    digits = [int(c) for c in code]
    check_digit = digits[9]

    weighted_sum = sum(digits[i] * (10 - i) for i in range(9))
    remainder = weighted_sum % 11

    if remainder < 2:
        return check_digit == remainder
    return check_digit == 11 - remainder


def validate_bulk(codes: Sequence[str]) -> List[bool]:
    """
    Validate a list of Iranian National Codes.

    Args:
        codes: A sequence of 10-digit strings.

    Returns:
        A list of booleans, in the same order as the input, where
        each entry is the validation result of the corresponding code.

    Example:
        >>> validate_bulk(["0499370899", "1111111111"])
        [True, False]
    """
    return [validate(code) for code in codes]
