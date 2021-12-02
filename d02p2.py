#!/usr/bin/env python3

import numpy as np
import pandas as pd


def solve() -> int:
    data_in = pd.read_csv("./data/d02/p1/input", header=None, delimiter=" ")

    x = data_in[1].where(data_in[0] == "forward").sum()

    # Apply sign information in-place
    data_in[1] = np.where(data_in[0] == "up", -data_in[1], data_in[1])

    # Prepare an up/down-only column for vectorized cumsum()
    data_in[2] = np.where(data_in[0] != "forward", data_in[1], np.nan)

    # Compute "aim"
    # -> ffill() carries over latest (i.e. non-NaN) result from cumsum() to data_in[0] == "forward" rows
    # -> fillna(0) zeroes the value in the first row, if NaN otherwise
    data_in[3] = data_in[2].cumsum().ffill().fillna(0)

    # Compute actual depth differences determined by "forward" moves, leave NaN elsewhere
    data_in[4] = np.where(data_in[0] == "forward", data_in[1] * data_in[3], np.nan)

    # Then, beautifully...
    depth = data_in[4].sum()

    return int(depth * x)


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
