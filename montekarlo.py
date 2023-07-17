from math import cos, pi
import random


""" Считаем интеграл $\int_{0}^{\pi} \frac{cos(x)}{x} \dot dx$"""


def montecarlo(n):
    a = 0
    b = pi
    points_number = 0
    for _ in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, 1)
        if y <= cos(x) / x:
            points_number += 1
    return pi * points_number / n


n = 100000
print(montecarlo(n))