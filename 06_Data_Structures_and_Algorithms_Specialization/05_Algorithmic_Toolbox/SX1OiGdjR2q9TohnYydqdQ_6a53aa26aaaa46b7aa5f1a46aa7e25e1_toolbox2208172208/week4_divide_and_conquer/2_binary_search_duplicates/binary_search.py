from typing import List

"""
7
2 4 4 4 7 7 9
4
9 4 5 2
"""


def binary_search(keys: List[int], query: int) -> int:
    low = 0
    high = len(keys) - 1
    indices = [-1]

    while low <= high:
        m = int((low + high) / 2)

        if keys[m] > query:
            high = m - 1
        elif keys[m] < query:
            low = m + 1
        else:
            # Keep searching in lower half.
            indices.append(m)
            high = m - 1

    if len(indices) == 1:
        return indices[0]
    else:
        idx = min(indices[1:])

    low = 0
    high = len(keys) - 1
    indices = [-1]

    while low <= high:
        m = int((low + high) / 2)

        if keys[m] > query:
            high = m - 1
        elif keys[m] < query:
            low = m + 1
        else:
            # Keep searching in upper half.
            indices.append(m)
            low = m + 1

    if len(indices) == 1:
        return indices[0]
    else:
        # Take the minimum of the results of lower and upper half.
        return min(min(indices[1:]), idx)


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
