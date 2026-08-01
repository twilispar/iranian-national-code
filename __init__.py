"""
iranian_national_code
======================

A small, dependency-free Python library to validate and generate
Iranian National Codes (کد ملی).

This is a Python port of the original JavaScript project:
https://github.com/majidh1/iranianNationalCode
"""

from .validator import validate
from .generator import generate, generate_round

__all__ = ["validate", "generate", "generate_round"]
__version__ = "1.0.0"
