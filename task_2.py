import math
import random
from typing import List, Optional


def filter_vectors(
        vectors_to_sort: List[List[int]],
        standard: List[int],
        sorted_vectors: Optional[List[List[int]]] = None,
        index=0
) -> List[List[int]]:
    if not sorted_vectors:
        sorted_vectors = []

    if index == len(vectors_to_sort):
        return sorted_vectors

    # Вычисление метрики Евклида
    distance: float = math.sqrt(
        (vectors_to_sort[index][0] - standard[0]) ** 2 +
        (vectors_to_sort[index][1] - standard[1]) ** 2 +
        (vectors_to_sort[index][2] - standard[2]) ** 2
    )

    # Проверка на соответствие условию и добавление в новый список, если нужно
    if distance <= 3:
        sorted_vectors.append(vectors_to_sort[index])

    # Рекурсивный вызов для следующего элемента
    return filter_vectors(
        vectors_to_sort=vectors_to_sort,
        standard=standard,
        sorted_vectors=sorted_vectors,
        index=index + 1
    )


def generate_vectors(vectors_size: int) -> List[List[int]]:
    """
    Генерация случайних векторов

    :param vectors_size: Размер векторов
    """

    return [
        [random.uniform(0, 10) for _ in range(3)]
        for _ in range(vectors_size)
    ]


def main():
    default_vectors: List[List[float]] = generate_vectors(10)
    standard_vector = [5, 5, 5]  # Эталон векторов
    filtered_vectors: List[List[int]] = filter_vectors(
        vectors_to_sort=default_vectors,
        standard=standard_vector
    )

    print(f"Исходные векторы: {default_vectors}")
    print(f"Отфильтрованные векторы: {filtered_vectors}")


if __name__ == "__main__":
    main()
