from math import factorial
from typing import List


def binomial_coefficient(n: int, k: int) -> float:
    return factorial(n) // (factorial(k) * factorial(n - k))


def main() -> None:
    N: int = 20  # Всего деталей в партии
    n: int = 12  # Стандартные детали в партии
    m: int = 6  # Отобранные детали

    p: List[float] = [
        binomial_coefficient(n=n, k=k) *
        binomial_coefficient(n=N - n, k=m - k) /
        binomial_coefficient(n=N, k=m) for k in range(m + 1)
    ]

    # Математическое ожидание M(x)
    Mx: float = sum(k * p[k] for k in range(m + 1))

    # M(x^2) для вычисления дисперсии
    Mx2: float = sum(k ** 2 * p[k] for k in range(m + 1))

    # Дисперсия D(x)
    Dx: float = Mx2 - Mx ** 2

    print(f"Математическое ожидание M(x): {Mx}")
    print(f"Дисперсия D(x): {Dx}")


if __name__ == "__main__":
    main()
