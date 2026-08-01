# iranian-national-code (Python)

A small, dependency-free Python library to validate and generate
Iranian National Codes (کد ملی).

Python port of the original JavaScript project by majidh1:
https://github.com/majidh1/iranianNationalCode

## Install

Copy the `iranian_national_code/` package into your project (no
external dependencies required).

## Usage

```python
from iranian_national_code import validate, generate, generate_round

validate("0499370899")   # -> True / False

generate()                # -> a random valid 10-digit code

generate_round()          # -> a random valid code with a "rounder" digit pattern
```

## API

| Function | Description |
|---|---|
| `validate(code: str) -> bool` | Checks the syntax and checksum of a national code. |
| `generate() -> str` | Generates a random, checksum-valid national code. |
| `generate_round() -> str` | Generates a random, checksum-valid code biased toward lower/repeated digits. |

## License

MIT — see [LICENSE](LICENSE). Original algorithm and project by
[majidh1](https://github.com/majidh1).

Python portal by [twilispar](https://github.com/twilispar)
