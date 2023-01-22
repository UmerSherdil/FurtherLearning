import random

from typing import List


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast_1(numbers: List[float]) -> float:
    sorted_numbers = sorted(numbers)

    return sorted_numbers[-1]*sorted_numbers[-2]


def max_pairwise_product_fast_2(numbers: List[float]) -> float:
    max_1, max_1_idx = numbers[0], 0

    for idx, num in enumerate(numbers[1:]):
        if num > max_1:
            max_1 = num
            max_1_idx = idx+1

    if max_1_idx == 0:
        max_2 = numbers[1]
    else:
        max_2 = numbers[0]

    for idx, num in enumerate(numbers):
        if idx == max_1_idx:
            continue
        else:
            if num > max_2:
                max_2 = num

    return max_1*max_2


def generate_random_list(n: int, highest_number: int) -> List[float]:
    return [random.randint(2, highest_number) for i in range(0, n)]


def perform_stress_test() -> None:
    while True:
        input_numbers = generate_random_list(100, 1000000)
        p1 = max_pairwise_product(input_numbers)
        p2 = max_pairwise_product_fast_2(input_numbers)

        if p1 == p2:
            print("OK")
        else:
            print(input_numbers)
            print(p1, p2)
            break


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product_fast_2(input_numbers))
    # perform_stress_test()
