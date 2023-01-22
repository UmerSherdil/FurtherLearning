import random


def fibonacci_number(n: int) -> int:
    if n <= 1:
        return n

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)


def fibonacci_number_fast_1(n: int) -> int:
    if n <= 1:
        return n
    else:
        result = [0]*(n+1)

        result[0] = 0
        result[1] = 1
        for i in range(2, n+1):
            result[i] = result[i-2] + result[i-1]

        return result[-1]


def fibonacci_number_fast_2(n: int) -> int:
    if n <= 1:
        return n
    else:
        previous = 0
        current = 1
        for _ in range(2, n+1):
            previous, current = current, previous + current
            # last_backup = last
            # last = previous_than_last + last
            # previous_than_last = last_backup

        return current


def get_random_n(highest_number: int) -> int:
    return random.randint(0, highest_number)


def perform_stress_test() -> None:
    while True:
        n = get_random_n(30)
        f1 = fibonacci_number(n)
        f2 = fibonacci_number_fast_2(n)

        if f1 == f2:
            print("OK")
        else:
            print(n)
            print(f1, f2)
            break


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number_fast_2(input_n))
    # perform_stress_test()