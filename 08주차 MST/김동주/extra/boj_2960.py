import math


def solve(n: int, k: int) -> int:
    # Sieve of Eratosthenes
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    sieve = [True] * (n+1)
    count = 0
    for P in range(2, n+1):
        if sieve[P]:
            for j in range(P, n+1, P):

                if sieve[j]:
                    count += 1
                    if count == k:
                        return j

                sieve[j] = False


if __name__ == "__main__":
    N, K = map(int, input().split())
    print(solve(N, K))