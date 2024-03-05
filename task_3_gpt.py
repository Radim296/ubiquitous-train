# Значения времени и данных
t = [1, 3, 5]
x = [2, 22, 66]


# Функция для интерполяции Лагранжа
def lagrange_interpolation(t, x, t_target):
    result = 0
    for i in range(len(t)):
        terms = 1
        for j in range(len(t)):
            if i != j:
                terms = terms * (t_target - t[j]) / (t[i] - t[j])
        result += terms * x[i]
    return result

