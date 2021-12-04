#!/usr/bin/env python3


def binarray2int(binarray) -> int:
    y: int = 0
    for i, j in enumerate(binarray[::-1]):
        y += j << i  # Bitwise equivalent to j*(2**i)
    return y


def no_op() -> None:
    # The no-op function; it should obviously be empty!
    pass


if __name__ == "__main__":
    no_op()
