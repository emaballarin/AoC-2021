#!/usr/bin/env python3


import numpy as np


def nan_like(array):
    tmp = np.empty_like(array)
    tmp.fill(np.nan)
    return tmp


def no_op() -> None:
    # The no-op function; it should obviously be empty!
    pass


if __name__ == "__main__":
    no_op()
