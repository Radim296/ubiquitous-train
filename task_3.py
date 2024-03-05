from typing import List


def main() -> None:
    t: List[int] = [1, 3, 5]
    x: List[int] = [2, 22, 66]

    x2: int = calculate(t=t, x=x, place_in_table=2)
    x4: int = calculate(t=t, x=x, place_in_table=4)

    print(f"{x2=}")
    print(f"{x4=}")


def calculate(t: List[int], x: List[int], place_in_table: int) -> int:
    """
    Вычисление по формуле

    :param t: Места в таблице
    :param x: Значения в таблице
    :param place_in_table: Место неизвестного коэффицента
    """

    result: int = 0

    for i in range(len(t)):
        terms: int = 1
        for j in range(len(t)):
            if i != j:
                terms = terms * (place_in_table - t[j]) / (t[i] - t[j])
        result += terms * x[i]
    return result


if __name__ == "__main__":
    main()
