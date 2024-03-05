import itertools

import numpy as np


def model(x: int, y: int) -> float:
    s: float = -1.4536 + 12.65 * x - 12.65 * y
    t: float = -17.0891 + 18.522 * x - 13.5775 * y
    p: float = 1 / (1 + np.exp(-s))
    q: float = 1 / (1 + np.exp(-t))
    z: float = 1 - 5.2788 * p + 6.5383 * q

    return z


def main() -> None:
    for x, y in itertools.product([0, 1], repeat=2):
        z = model(x=x, y=y)
        print(f"Вывод: ({x=}, {y=}) => {z=}")

    for x, y in itertools.product([0, 1], repeat=2):
        z = model(x=x, y=y)
        classified_output: int = 1 if z >= 0.5 else 0
        print(f"Вывод: ({x=}, {y=}) => {classified_output=}")


if __name__ == "__main__":
    main()
