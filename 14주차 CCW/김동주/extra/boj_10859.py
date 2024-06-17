# 뒤집어진 소수

from typing import List


def is_prime(n: int) -> int:
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5)+1):
        if sieve[i]:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    return sieve[n]


def rotate_180(d: int) -> int:
    return (0, 1, 2, None, None, 5, 9, None, 8, 6)[d]


def concat_digits(digits: List[int]) -> int:
    result = 0
    for d in digits:
        result *= 10
        result += d
    return result


if __name__ == "__main__":
    N = list(map(int, input().strip()))
    N_rev = list(map(rotate_180, reversed(N)))
    if (None in N_rev) or (not is_prime(concat_digits(N_rev))):
        print('no')
    else:
        print('yes')
