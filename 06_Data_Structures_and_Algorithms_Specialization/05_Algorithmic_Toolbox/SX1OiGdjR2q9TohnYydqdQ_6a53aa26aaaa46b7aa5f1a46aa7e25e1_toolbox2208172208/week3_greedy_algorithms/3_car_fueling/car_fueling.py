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

    return -1


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
