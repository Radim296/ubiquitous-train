from math import factorial


def binomial_coefficient(n: int, k: int) -> float:
    """Вычисление коэффициента Биномиального распределения"""

    return factorial(n) / (factorial(k) * factorial(n - k))


def p_func(n: int, k: int, p: float):
    q: float = 1 - p
    return binomial_coefficient(n=n, k=k) * (p ** k) * (q ** (n - k))


def calculate_sum(n: int, k: int, p: float) -> float:
    P_A: float = sum(p_func(n=n, k=i, p=p) for i in range(k))
    P_B: float = sum(p_func(n=n, k=i, p=p) for i in range(k + 1, n + 1))
    P_C: float = sum(p_func(n=n, k=i, p=p) for i in range(k, n + 1))
    P_D: float = sum(p_func(n=n, k=i, p=p) for i in range(k + 1))

    return P_A * P_B + P_C * P_D


def main() -> None:
    n: int = 8
    k: int = 5
    p: float = 0.5  # Задаем некоторое значение p, так как коэффициент не указан в условии задачи
    result: float = calculate_sum(n=n, k=k, p=p)

    print(f"Сумма вероятностей P(A)*P(B) + P(C)*P(D) = {result}")


if __name__ == "__main__":
    main()
