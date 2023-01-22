import random

def gcd(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_fast(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        remainder = a % b
        return gcd_fast(b, remainder)


def get_random_n(highest_number: int) -> int:
    return random.randint(1, highest_number)


def perform_stress_test() -> None:
    while True:
        n1 = get_random_n(30)
        n2 = get_random_n(30)
        f1 = gcd(n1, n2)
        f2 = gcd_fast(n1, n2)

        if f1 == f2:
            print("OK")
        else:
            print(n1, n2)
            print(f1, f2)
            break

if __name__ == "__main__":
    a, b = map(int, input().split())
    c = gcd_fast(a, b)
    print(c)
    # perform_stress_test()
