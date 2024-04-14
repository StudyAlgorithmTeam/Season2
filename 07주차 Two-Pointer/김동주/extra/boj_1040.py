import functools
import sys


N: int
K: int


@functools.cache
def dp(n: int, deg: int, flag: int) -> int:
    """10진수 deg자리 수인 n 보다 크거나 같은 수 중 K개의 숫자로 이루어진 수를 찾음

    단, deg 앞 자리 수에서 flag에 표기된 숫자들은 이미 사용 된 것으로 가정.

    n <= 10^18
    deg <= 18
    flag < 2^10
    """
    k = get_k(flag)
    if k > K:
        return None
    if deg == 0:
        return None if k != K else 0

    base = 10 ** (deg-1)
    msb = n // base
    rem = n % base # remainder

    while msb < 10:
        if (ans := dp(rem, deg-1, flag | (1 << msb))) is not None:
            return (msb * base) + ans
        msb += 1
        rem = 0

    return None


def get_deg(n: int) -> int:
    """n이 몇 자릿 수인지 반환"""
    deg = 0
    while n:
        deg += 1
        n //= 10
    return deg


def get_k(flag: int) -> int:
    """플래그를 보고 지금까지 사용된 숫자의 개수를 반환"""
    k = 0
    for i in range(10):
        if (flag & (1 << i)):
            k += 1
    return k


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())

    n = N
    deg = get_deg(n)
    # 해보고 안 되면 자릿 수 늘려서 다시 해보기
    while (ans := dp(n, deg, 0)) is None:
        n = 10 ** deg
        deg += 1

    sys.stdout.write(f'{ans}\n')
