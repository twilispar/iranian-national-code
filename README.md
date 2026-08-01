# iranian-national-code

A small, dependency-free Python library to validate and generate
Iranian National Codes (کد ملی).

Python port of the original JavaScript project by majidh1:
https://github.com/majidh1/iranianNationalCode

## Install

Using [uv](https://docs.astral.sh/uv/) (recommended):

```bash
uv add iranian-national-code
```

Using pip:

```bash
pip install iranian-national-code
```

## Usage

```python
from iranian_national_code import (
    validate,
    validate_bulk,
    generate,
    generate_round,
    generate_bulk,
)

# Validate a single code
validate("0499370899")          # -> True / False

# Validate many codes at once
validate_bulk(["0499370899", "1111111111"])   # -> [True, False]

# Generate a single random valid code
generate()                      # -> e.g. "8856815311"

# Generate a code with a "rounder" digit pattern
generate_round()                # -> e.g. "6510101017"

# Generate many codes at once
generate_bulk(5)                # -> list of 5 valid codes
generate_bulk(5, round_style=True)  # -> list of 5 "round" codes
```

## API

| Function | Description |
|---|---|
| `validate(code: str) -> bool` | Checks the syntax and checksum of a single national code. |
| `validate_bulk(codes: list[str]) -> list[bool]` | Validates a list of codes, returning a matching list of booleans. |
| `generate() -> str` | Generates a random, checksum-valid national code. |
| `generate_round() -> str` | Generates a random, checksum-valid code biased toward lower/repeated digits. |
| `generate_bulk(count: int, round_style: bool = False) -> list[str]` | Generates `count` random, checksum-valid codes. |

## Development

This project uses [uv](https://docs.astral.sh/uv/) for dependency
management and packaging.

```bash
git clone https://github.com/twilispar/iranian-national-code.git
cd iranian-national-code
uv sync
uv build
```

## License

MIT — see [LICENSE](LICENSE). Original algorithm and project by
[majidh1](https://github.com/majidh1).
