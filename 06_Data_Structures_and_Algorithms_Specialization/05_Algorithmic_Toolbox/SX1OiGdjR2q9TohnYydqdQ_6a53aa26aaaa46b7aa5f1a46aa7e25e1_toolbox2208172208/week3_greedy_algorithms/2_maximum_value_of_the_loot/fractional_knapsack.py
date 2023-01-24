from sys import stdin

from typing import List


def shop_empty(weights: List[int]) -> bool:
    return True if len([item for item in weights if item != 0.0]) == 0 else False


def optimal_value(capacity: int, weights: List[int], values: List[int]) -> float:
    # 3 50 60 20 100 50 120 30
    # 1 1000 500 30
    value = 0.
    # write your code here
    value_per_unit_weight = [v / w for w, v in zip(weights, values)]
    value_per_unit_weight_sorted = sorted(value_per_unit_weight, reverse=True)

    value_per_unit_weight_sorted_idx = [value_per_unit_weight.index(item) for item in value_per_unit_weight_sorted]

    sorted_values_and_weights = list(zip(values, weights))
    sorted_values_and_weights_sorted = [sorted_values_and_weights[i] for i in value_per_unit_weight_sorted_idx]
    sorted_values_and_weights_sorted = [list(item) for item in sorted_values_and_weights_sorted]

    while capacity > 0:
        for idx, (v, w) in enumerate(sorted_values_and_weights_sorted):
            if w != 0:
                if capacity < w: # 20 50
                    added_weight = capacity
                    capacity = capacity - added_weight
                    value = value + added_weight*(v/w)
                else: # 50 20
                    added_weight = w
                    capacity = capacity - added_weight
                    value = value + v

                sorted_values_and_weights_sorted[idx][1] = w - added_weight

        if shop_empty([w for _, w in sorted_values_and_weights_sorted]):
            break

    return value


def optimal_value_recursive(capacity: int, weights: List[int], values: List[int]) -> float:
    if capacity == 0 or len(weights) == 0:
        return 0

    value_per_unit_weight = [v / w for w, v in zip(weights, values)]
    most_expensive = max(value_per_unit_weight)
    m = value_per_unit_weight.index(most_expensive)
    amount = min(weights[m], capacity)
    value = amount*(value_per_unit_weight[m])
    weights.pop(m)
    values.pop(m)

    return value + optimal_value_recursive(capacity-amount, weights, values)


if __name__ == "__main__":
    # data = list(map(int, input().split()))
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value_recursive(capacity, weights, values)
    print("{:.10f}".format(opt_value))