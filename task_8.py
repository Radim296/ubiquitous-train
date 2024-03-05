import numpy as np


def main() -> None:
    t = np.array([1, 2, 3, 4, 5, 6])
    x = np.array([1.0, 1.5, 3.0, 4.5, 8.0, 13.5])

    n: int = len(t)

    t2 = t ** 2
    t3 = t ** 3
    t4 = t ** 4

    sum_t = np.sum(t)
    sum_t2 = np.sum(t2)
    sum_t3 = np.sum(t3)
    sum_t4 = np.sum(t4)

    sum_tx = np.sum(t * x)
    sum_t2x = np.sum(t2 * x)
    A = np.array(
        [
            [sum_t4, sum_t3, sum_t2],
            [sum_t3, sum_t2, sum_t],
            [sum_t2, sum_t, n]
        ]
    )

    B = np.array([sum_t2x, sum_tx, np.sum(x)])
    coefficients = np.linalg.solve(A, B)
    a, b, c = coefficients

    print(f"Коэффициенты регрессионной модели:\na = {a}, b = {b}, c = {c}")


if __name__ == "__main__":
    main()
