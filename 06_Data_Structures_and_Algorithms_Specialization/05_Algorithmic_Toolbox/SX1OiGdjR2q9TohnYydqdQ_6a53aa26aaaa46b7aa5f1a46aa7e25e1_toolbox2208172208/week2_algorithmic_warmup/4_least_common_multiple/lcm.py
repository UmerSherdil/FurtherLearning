import random


def lcm(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    assert False


def lcm_fast(a: int, b: int) -> int:
    if a == b:
        return a
    elif a > b:
        bigger = a
        smaller = b
    else:
        bigger = b
        smaller = a

    n = 1
    while True:
        lcm = bigger*n
        if lcm % smaller == 0:
            return lcm
        n += 1


def get_random_n(highest_number: int) -> int:
    return random.randint(1, highest_number)


def perform_stress_test() -> None:
    while True:
        n1 = get_random_n(3000)
        n2 = get_random_n(3000)
        r1 = lcm(n1, n2)
        r2 = lcm_fast(n1, n2)

        if r1 == r2:
            print("OK")
        else:
            print(n1, n2)
            print(r1, r2)
            break


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_fast(a, b))
    # perform_stress_test()
