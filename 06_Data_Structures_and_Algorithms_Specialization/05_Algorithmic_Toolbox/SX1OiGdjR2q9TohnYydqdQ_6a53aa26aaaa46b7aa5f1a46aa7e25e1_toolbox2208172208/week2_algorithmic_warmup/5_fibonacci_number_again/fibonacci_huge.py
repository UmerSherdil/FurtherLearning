# Not done.
# Task involves understanding of Pisano period.

import random

import time


def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)

    return current % m


def fibonacci_huge_fast(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current % m, (previous + current) % m

    return current % m


def get_random_n(highest_number: int) -> int:
    return random.randint(1, highest_number)


def perform_stress_test() -> None:
    while True:
        n1 = get_random_n(30)
        n2 = get_random_n(30)
        f1 = fibonacci_huge_naive(n1, n2)
        f2 = fibonacci_huge_fast(n1, n2)

        if f1 == f2:
            print("OK")
        else:
            print(n1, n2)
            print(f1, f2)
            break


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
    # perform_stress_test()


'''
5 + 8 = 13 (1 + 2 != 4)
a + b = c
(a % m + b % m) % m = c % m
r_a + r_b = r_c
(m*q - a) + (m*q - b) = m*q - c
m*(q_a + q_b - q_c) = a + b - c
m*(q_a + q_b - q_c) = 0
m != 0
-> (q_a + q_b - q_c) = 0

a / m + b / m = c / m
'''