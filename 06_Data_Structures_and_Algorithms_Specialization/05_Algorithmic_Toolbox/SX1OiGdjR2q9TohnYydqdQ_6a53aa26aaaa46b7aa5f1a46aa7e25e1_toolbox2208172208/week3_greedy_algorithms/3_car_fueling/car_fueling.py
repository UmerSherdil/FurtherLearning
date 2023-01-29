from sys import stdin

from typing import List


def min_refills(distance: int, tank: int, stops: List[int]) -> int:
    distance_travelled = 0
    refuel = 0
    current_tank = tank
    i = 0
    while distance_travelled < distance and i <= len(stops)-1:
        # Distance to the previous stop.
        if i == 0:
            delta_d_previous = stops[i]
        else:
            delta_d_previous = stops[i] - stops[i-1]

        # Distance to the next stop.
        if i == len(stops)-1:
            delta_d_next = distance - stops[i]
        else:
            delta_d_next = stops[i + 1] - stops[i]

        if tank < delta_d_previous:
            # print("Tank empties between stops!")
            return -1

        # Current tank is based on the distance to the previous stop.
        current_tank -= delta_d_previous

        # Refueling is based upon the distance to the next stop.
        need_to_refuel = True if current_tank - delta_d_next < 0 else False
        if need_to_refuel:
            refuel += 1
            current_tank = tank

        distance_travelled += delta_d_previous
        i += 1

    if i == len(stops) and current_tank < distance - distance_travelled:
        # print("Tank empties in the last stretch!")
        refuel = -1

    return refuel

if __name__ == '__main__':
    # d, m, _, *stops = list(map(int, input().split()))
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))