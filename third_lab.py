import math

ITERATIONS = 20

def my_sin(x):
    """
    Вычисление синуса при помощи частичного суммирования
    ряда Тейлора для окрестности 0
    """
    x_pow = x
    multiplier = 1
    partial_sum = x
    for n in range(1, ITERATIONS):
        x_pow *= x**2  # В цикле постепенно считаем степень
        multiplier *= -1 / (2*n) / (2*n + 1)  # (-1)^n и факториал
        partial_sum += x_pow * multiplier
    
    return partial_sum

help(math.sin)
help(my_sin)

print(math.sin(0.4))
print(my_sin(0.4))