from math import factorial


def binomial_coefficient(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def P(n, k, p):
    q = 1 - p
    return binomial_coefficient(n, k) * (p ** k) * (q ** (n - k))


# Параметры задачи
n = 8
k = 5
p = 0.5  # Задаем некоторое значение p, так как коэффициент p не указан в условии задачи

# Вероятности
P_A = sum(P(n, i, p) for i in range(k))  # менее k раз
P_B = sum(P(n, i, p) for i in range(k + 1, n + 1))  # более k раз
P_C = sum(P(n, i, p) for i in range(k, n + 1))  # не менее k раз
P_D = sum(P(n, i, p) for i in range(k + 1))  # не более k раз, включая k

# Вычисление искомой суммы вероятностей
result = P_A * P_B + P_C * P_D

print(f"Сумма вероятностей P(A)*P(B) + P(C)*P(D) = {result}")
