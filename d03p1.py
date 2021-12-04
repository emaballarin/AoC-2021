#!/usr/bin/env python3

from functools import partial as fpartial
import numpy as np
from util.transforms import binarray2int
from util.specifics import binary_abundance


def solve() -> int:
    # Transposition eases operating over rows w.r.t. over columns
    data_in = np.genfromtxt("./data/d03/p1/input", delimiter=1).transpose()

    # Original (i.e. pre-transposition) number of rows
    data_len = len(data_in[0])

    # Number of 1s is sum at that position; number of 0s is number of elements - number of 1s
    gamma = np.apply_along_axis(
        fpartial(binary_abundance, col_len=data_len), 1, data_in
    )

    # (Binary complement, done with integers)
    epsilon = 1 - gamma

    consumption = binarray2int(epsilon) * binarray2int(gamma)
    return consumption


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
