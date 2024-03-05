from math import factorial


# Функция для вычисления биномиальных коэффициентов
def binom(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


# Заданные параметры
N = 20  # Всего деталей в партии
n = 12  # Стандартные детали в партии
m = 6  # Отобранные детали

# Вероятности для каждого возможного значения x
p = [binom(n, k) * binom(N - n, m - k) / binom(N, m) for k in range(m + 1)]

# Математическое ожидание M(x)
Mx = sum(k * p[k] for k in range(m + 1))

# M(x^2) для вычисления дисперсии
Mx2 = sum(k ** 2 * p[k] for k in range(m + 1))

# Дисперсия D(x)
Dx = Mx2 - Mx ** 2

print(f"Математическое ожидание M(x): {Mx}")
print(f"Дисперсия D(x): {Dx}")
