import random
from typing import List


def simulate_discrete_variable(values: List[int], probabilities: List[float]) -> int:
    assert len(values) == len(probabilities), "Количество значений и вероятностей должно совпадать"
    assert abs(sum(probabilities) - 1) < 1e-6, "Сумма вероятностей должна быть равна 1"

    n: float = random.random()

    accumulated_probability: int = 0
    for value, probability in zip(values, probabilities):
        accumulated_probability += probability
        if n <= accumulated_probability:
            return value

    return values[-1]


def main() -> None:
    values: List[int] = [2, 10, 18]
    probabilities: List[float] = [0.22, 0.17, 0.61]
    simulated_value: int = simulate_discrete_variable(values=values, probabilities=probabilities)
    print(f"Разыгранное значение: {simulated_value}")


if __name__ == "__main__":
    main()
