#!/usr/bin/env python3

import pandas as pd


def solve() -> int:
    data_in = pd.read_csv("./data/d02/p1/input", header=None, delimiter=" ")
    depth = (
        data_in[1].where(data_in[0] == "down").sum()
        - data_in[1].where(data_in[0] == "up").sum()
    )
    x = data_in[1].where(data_in[0] == "forward").sum()

    return int(depth * x)


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
