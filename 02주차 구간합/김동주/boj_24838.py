from sys import stdin
from sys import stdout
from functools import cache
from functools import reduce
from typing import Iterable


MOD = int(1e9+7)


def madd(a: int, b: int, mod=MOD) -> int:
    return ((a % mod) + (b % mod)) % mod


def mmul(a: int, b: int, mod=MOD) -> int:
    """나머지가 있는 곱을 구하는 함수.
    (A * B) mod C = (A mod C * B mod C) mod C

    https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-multiplication
    """
    return ((a % mod) * (b % mod)) % mod


def msum(x: Iterable[int], mod=MOD) -> int:
    return reduce(madd, x)


@cache
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return mmul(factorial(n-1), n)


def testcase():
    # 핵심 아이디어: 가장 많이 포함된 구간에 큰 숫자 배정
    # 나머지연산은 덧셈, 곱셈에 대해 분배법칙이 적용됨에 주목할 것.

    n, m = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))
    A_cnt = [0] * n # A의 각 원소가 포함된 구간의 개수

    # O(n * m)
    for j in range(m):
        x, y = map(int, stdin.readline().split())
        for i in range(x-1, y): # y-x 는 최대 n
            A_cnt[i] += 1

    # O(n log n) 기본적으로 오름차순 정렬
    A.sort()
    A_cnt.sort()

    max_s = 0
    n_cases = 1

    while A_cnt and A_cnt[-1] != 0:
        count = A_cnt.pop() # A의 한 원소가 포함된 구간의 개수
        length = 1 # 같은 count 값을 갖는 구간의 길이

        a = A.pop()
        while A_cnt and A_cnt[-1] == count:
            a = madd(a, A.pop())
            A_cnt.pop()
            length += 1

        max_s = madd(max_s, mmul(a, count))
        n_cases = mmul(n_cases, factorial(length))

    # 아무 구간에도 포함하지 않은 원소를 배치하는 경우의 수 계산
    length = len(A_cnt)
    n_cases = mmul(n_cases, factorial(length))

    stdout.write(f'{max_s} {n_cases}\n')


if __name__ == "__main__":
    for t in range(int(stdin.readline())):
        testcase()
