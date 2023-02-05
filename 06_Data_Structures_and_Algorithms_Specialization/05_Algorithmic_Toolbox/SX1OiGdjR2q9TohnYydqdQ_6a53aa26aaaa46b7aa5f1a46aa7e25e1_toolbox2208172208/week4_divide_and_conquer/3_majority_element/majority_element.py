from typing import List

# https://www.geeksforgeeks.org/majority-element/
def majority_element_naive(elements: List[float]) -> int:
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def find_majority(arr: List[float], size: int) -> int:
    m = {}
    for i in range(size):
        if arr[i] in m:
            m[arr[i]] += 1
        else:
            m[arr[i]] = 1

    is_majority_present = False
    for key in m:
        if m[key] > size / 2:
            is_majority_present = True
            break
    if is_majority_present:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(find_majority(input_elements, len(input_elements)))
