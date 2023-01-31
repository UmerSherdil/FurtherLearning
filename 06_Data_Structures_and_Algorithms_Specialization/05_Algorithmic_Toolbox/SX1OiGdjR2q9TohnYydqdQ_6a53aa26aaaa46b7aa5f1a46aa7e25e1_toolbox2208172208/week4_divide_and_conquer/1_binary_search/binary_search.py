import bisect
import random
from typing import List


def binary_search(keys: List[int], query: int) -> int:
    pos = bisect.bisect_left(keys, query)
    return pos if pos != len(keys) and keys[pos] == query else -1


def binary_search_manual(keys: List[int], query: int) -> int:
    low = 0
    high = len(keys)-1
    idx = -1

    while low <= high:
        m = int((low+high)/2)

        if keys[m] > query:
            high = m - 1
        elif keys[m] < query:
            low = m + 1
        else:
            idx = m
            break

    return idx


def generate_random_list(n: int, highest_number: int) -> List[int]:
    return [random.randint(2, highest_number) for _ in range(0, n)]


def perform_stress_test() -> None:
    while True:
        input_numbers = generate_random_list(10, 1000000)
        test_number = generate_random_list(1, 1000000)[0]
        p1 = binary_search(sorted(input_numbers), test_number)
        p2 = binary_search_manual(sorted(input_numbers), test_number)

        if p1 == p2:
            print("OK")
        else:
            print(input_numbers)
            print(p1, p2)
            break


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = sorted(list(map(int, input().split())))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search_manual(input_keys, q), end=' ')

    # perform_stress_test()
