import collections
import sys
import typing



N: typing.List[int]
K: int

COUNTER = collections.Counter()


def dp(i: int, k: int, carry: bool = False) -> bool:
    if i == -1:
        return k == 0
    old_val = N[i]
    s = 0 if carry else N[i]
    for n in range(s, 10):
        if COUNTER[n] == 0:
            k -= 1
        COUNTER[n] += 1

        N[i] = n
        if dp(i-1, k, carry):
            return True
        carry = True

        COUNTER[n] -= 1
        if COUNTER[n] == 0:
            k += 1
    N[i] = old_val
    return False


if __name__ == '__main__':
    N, K = sys.stdin.readline().split()
    N = list(map(int, reversed(N)))
    K = int(K)
    dp(len(N)-1, K)
    sys.stdout.write(f'{"".join(map(str, reversed(N)))}\n')
