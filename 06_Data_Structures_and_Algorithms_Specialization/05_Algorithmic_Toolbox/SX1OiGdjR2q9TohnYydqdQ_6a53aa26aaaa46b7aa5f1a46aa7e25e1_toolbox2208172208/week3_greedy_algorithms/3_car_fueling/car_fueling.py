from sys import stdin

from typing import List


def min_refills(distance: int, tank: int, stops: List[int]) -> int:
    # write your code here
    '''
    :param distance:
    :param tank:
    :param stops:
    :return:
    Q1: Need a refill? -> Compare the mileage with the farthest gas station -> If the mileage is more than distance -> No need to refill.
    Q2: If mileage - (Distance of petrol station + Distance to the next petrol station) > mileage -> If yes -> Need refill, other no.
    Q3: If the mileage is less than the distance between two conseutive fuel stations before the distance cover has been met -> If yes -> -1 as the distance cannot be conveed even with refueling.
    Till the distance is not reached or the n
    '''

    '''
    950
    400
    4
    200 375 550 750
    '''
    _stops = [0] + stops + [distance]
    distance_between_stops = [b-a for a, b in zip(stops[:-1], stops[1:])] # what if this list becomes emtpy.
    if tank >= stops[-1]:
        return 0
    elif tank < max(distance_between_stops):
        return -1
    elif tank < stops[0]:
        return -1
    else:
        previous_tank = tank
        distance_travelled = 0
        delta_d = 0
        refuel = 0
        while distance_travelled < distance:
            current_tank = previous_tank - delta_d
            delta_d = distance_between_stops.pop(0)
            if current_tank - delta_d < 0:
                previous_tank = tank
                refuel += 1
            else:
                previous_tank = current_tank
            distance_travelled += delta_d

        return refuel


if __name__ == '__main__':
    # d, m, _, *stops = list(map(int, input().split()))
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))