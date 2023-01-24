import random

# Implement this thing as a recursive algorithm.

def change(money: int) -> int:
    # write your code here
    coins = 0
    while money != 0:
        if money - 10 >= 0:
            money -= 10
            coins += 1
        elif money - 5 >= 0:
            money -= 5
            coins += 1
        else:
            money -= 1
            coins += 1

    return coins


def change_second(money: int) -> int:
    return int(money / 10) + int((money % 10) / 5) + money % 5


def get_random_n(highest_number: int) -> int:
    return random.randint(0, highest_number)


def perform_stress_test() -> None:
    while True:
        n = get_random_n(100234)
        f1 = change(n)
        f2 = change_second(n)

        if f1 == f2:
            print("OK")
        else:
            print(n)
            print(f1, f2)
            break


if __name__ == '__main__':
    # m = int(input())
    # print(change_second(m))
    perform_stress_test()
