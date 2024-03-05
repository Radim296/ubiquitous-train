import math
import random


# Рекурсивная функция фильтрации
def filter_vectors(vectors, standard, close=[], index=0):
    # Условие окончания рекурсии
    if index == len(vectors):
        return close

    # Вычисление метрики Евклида
    distance = math.sqrt((vectors[index][0] - standard[0]) ** 2 + (vectors[index][1] - standard[1]) ** 2 + (
            vectors[index][2] - standard[2]) ** 2)

    # Проверка на соответствие условию и добавление в новый список, если нужно
    if distance < 3:
        close.append(vectors[index])

    # Рекурсивный вызов для следующего элемента
    return filter_vectors(vectors, standard, close, index + 1)


# Генерация списка случайных векторов
def generate_vectors(n):
    return [[random.uniform(0, 10) for _ in range(3)] for _ in range(n)]


# Основная функция
def main():
    # Генерация исходного списка векторов
    S = generate_vectors(10)
    # Задаем эталонный вектор
    v_standard = [5, 5, 5]
    # Вызов функции фильтрации
    filtered_vectors = filter_vectors(S, v_standard)
    print("Исходные векторы:", S)
    print("Прошедшие фильтр:", filtered_vectors)


if __name__ == "__main__":
    main()
