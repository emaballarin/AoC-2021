import numpy as np
from util.transforms import binarray2int
from util.specifics import binary_abundance_sieve


def solve() -> int:
    data_in = np.genfromtxt("./data/d03/p1/input", delimiter=1)

    # We need some copies as our sieves operate in-place
    data_most, data_least = np.copy(data_in), np.copy(data_in)

    # Most of the complexity is hidden into implementation
    return binarray2int(binary_abundance_sieve(data_most, "most")) * binarray2int(
        binary_abundance_sieve(data_least, "least")
    )


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
