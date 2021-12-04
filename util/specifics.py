#!/usr/bin/env python3


import numpy as np
from util.nputils import nan_like


def binary_abundance(col, col_len, ranking="most"):
    if ranking == "most":
        # The number of 1s (in 1s and 0s) is the highest if their sum exceeds
        # half the total number of digits. If not, 0s are the most abundant.
        return np.where(col.sum() >= col_len / 2, 1, 0)

    if ranking == "least":
        # Binary complement, done with integers
        # Fixed 1-deep recursion not a problem (but keeps implementation unique)
        return 1 - binary_abundance(col, col_len, ranking="most")

    raise ValueError(f"'ranking' must be either 'most' or 'least'. Given: {ranking}")


def binary_abundance_sieve(array, ranking):
    # As in any sieve, we iterate. Here: over the position of considered bit
    bit_idx = 0
    while len(array) > 1:

        # Since the sieve reduces the number of "data", we need to re-compute
        # rolling quantities: length and binary abundance (of the varying index)
        data_len = len(array)
        criterion = binary_abundance(array[:, bit_idx], data_len, ranking)

        # Binary numbers not matching the criterion are replaced with all-NaN
        # sub-arrays...
        array = np.apply_along_axis(
            lambda elem, criterion=criterion, bit_idx=bit_idx: np.where(
                elem[bit_idx] == criterion, elem, nan_like(elem)
            ),
            1,
            array,
        )

        # ... which are then removed from the overall "matrix"
        array = array[~np.isnan(array).any(axis=1)]

        bit_idx += 1

    return array[0].astype(dtype=np.int)


def no_op() -> None:
    # The no-op function; it should obviously be empty!
    pass


if __name__ == "__main__":
    no_op()
