import sys


# pre-calculated primes

MAX_SIEVE = int(1e6)


sieve = [True] * (MAX_SIEVE + 1)
i = 2
while (i*i) <= MAX_SIEVE:
    if sieve[i]:
        for j in range(2*i, MAX_SIEVE+1, i):
            sieve[j] = False
    i += 1

prime = [i for i in range(2, MAX_SIEVE+1) if sieve[i]]


def count_square_free(nth_prime: int, x: int, end: int) -> int:
    x_next = x * prime[nth_prime] * prime[nth_prime]
    if x_next > end:
        return 0
    count = end // x_next
    inclusion = count_square_free(nth_prime+1, x, end)
    exclusion = count_square_free(nth_prime+1, x_next, end)
    return count + inclusion - exclusion


if __name__ == "__main__":
    sys.setrecursionlimit(MAX_SIEVE)

    MAX_K = int(1e12)
    K = int(input())

    # 이분 탐색에 O(log K)
    start = 1
    end = MAX_K
    while start < end:
        mid = (start+end) // 2
        count = count_square_free(0, 1, mid)
        count = mid - count
        if count < K:
            start = mid + 1
        else:
            end = mid

    print(start)
