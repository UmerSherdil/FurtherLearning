from sys import stdin
from typing import List
import numpy as np


def optimal_value(capacity: int, weights: List[int], values: List[int]) -> int:
    # 3 50 60 20 100 50 120 30
    value = 0.
    # write your code here
    # Sort the bug for the first example data
    value_per_unit_weight = [v / w for w, v in zip(weights, values)]
    value_per_unit_weight_sorted = sorted(value_per_unit_weight, reverse=True)

    value_per_unit_weight_sorted_idx = [value_per_unit_weight.index(item) for item in value_per_unit_weight_sorted]

    sorted_values_and_weights = list(zip(values, weights))
    sorted_values_and_weights_sorted = [sorted_values_and_weights[i] for i in value_per_unit_weight_sorted_idx]

    while capacity > 0:
        for v, w in sorted_values_and_weights_sorted:
            if w != 0:
                if capacity < w:
                    added_weight = capacity
                    capacity = capacity - added_weight
                    value = value + added_weight*(v/w)
                elif capacity >= w:
                    added_weight = w
                    capacity = capacity - added_weight
                    value = value + v

    return value


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
