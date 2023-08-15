import timeit

import numpy as np
from scipy.optimize import curve_fit
from numba import njit


@njit
def karatsuba(x: int, y: int):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        m: int = max(len(str(x)), len(str(y)))
        m2: float = m / 2

        a = int(x / 10 ** m2)
        b = int(x % 10 ** m2)
        c = int(y / 10 ** m2)
        d = int(y % 10 ** m2)

        z0 = karatsuba(b, d)
        z1 = karatsuba((a + b), (c + d))
        z2 = karatsuba(a, c)

        return (z2 * 10 ** (2 * m2)) + ((z1 - z2 - z0) * 10 ** m2) + z0


def test_karatsuba():
    num_runs = 10

    # Задаем список для хранения времен выполнения
    execution_times = []

    # Запускаем заданное количество раз алгоритм и сохраняем время каждого запуска
    for _ in range(num_runs):
        start_time = timeit.default_timer()
        result = karatsuba(123456789, 987654321)
        execution_time = timeit.default_timer() - start_time
        execution_times.append(execution_time)

    # Вычисляем лучшее, худшее и среднее время выполнения
    best_time = min(execution_times)
    worst_time = max(execution_times)
    average_time = sum(execution_times) / num_runs

    print("Результат умножения:", result)
    print("Лучшее время выполнения:", best_time, "секунд")
    print("Худшее время выполнения:", worst_time, "секунд")
    print("Среднее время выполнения:", average_time, "секунд")


def linear_model(v, a, b):
    return a * v + b


def quadratic_model(v, a, b):
    return a * v * v + b * v


def binary_search(a: list, x) -> bool:
    lo, hi = 0, len(a) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid - 1
        elif x > a[mid]:
            lo = mid + 1
        else:
            return True
    return False


def binary_search_idx(a: list, x) -> int:
    lo, hi = 0, len(a) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        diff = x - a[mid]
        if diff < 0:
            hi = mid - 1
        elif diff > 0:
            lo = mid + 1
        else:
            return mid
    return -(lo + 1)


if __name__ == "__main__":
    xs = np.array((100, 1000, 10000))
    ys = np.array((0.063, 0.565, 5.946))

    (a, b), _ = curve_fit(quadratic_model, xs, ys)

    test_karatsuba()
