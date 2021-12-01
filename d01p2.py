#!/usr/bin/env python3

import numpy as np


def solve() -> int:
    data_in = np.genfromtxt("./data/d01/p1/input")
    windowed = np.convolve(data_in, np.ones(3, dtype=int), mode="valid")
    ret = np.count_nonzero(np.diff(windowed) > 0)
    return int(ret)


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
