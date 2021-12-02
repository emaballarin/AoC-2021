#!/usr/bin/env python3

import numpy as np


def solve() -> int:
    data_in = np.loadtxt("./data/d01/p1/input")
    ret = np.count_nonzero(np.diff(data_in) > 0)
    return int(ret)


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
