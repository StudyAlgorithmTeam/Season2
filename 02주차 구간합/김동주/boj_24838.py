from sys import stdin
from sys import stdout


MOD = int(1e9+7)
MAX_N = 50000
MOD_FACTORIAL = []


"""
나머지의 분배법칙 이용

    (A * B) mod C = (A mod C * B mod C) mod C

    https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-multiplication
"""
def madd(a: int, b: int, mod=MOD) -> int:
    return ((a % mod) + (b % mod)) % mod


def mmul(a: int, b: int, mod=MOD) -> int:
    return ((a % mod) * (b % mod)) % mod


def init_mod_factorial():
    # O(n)
    MOD_FACTORIAL.append(1)
    for i in range(1, MAX_N+1):
        MOD_FACTORIAL.append(mmul(MOD_FACTORIAL[-1], i))


def testcase():
    # 핵심 아이디어: 가장 많이 포함된 구간에 큰 숫자 배정
    # 나머지연산은 덧셈, 곱셈에 대해 분배법칙이 적용됨에 주목할 것.

    n, m = map(int, stdin.readline().split())

    # O(n log n)
    A = list(map(int, stdin.readline().split()))
    A.sort()

    # O(m)
    events = []
    for j in range(m):
        x, y = map(int, stdin.readline().split())
        events.append((x, +1)) # rising edge
        events.append((y+1, -1)) # falling edge
    # O(m log m)
    events.sort()

    # O(m)
    frequency = [0] * (m + 1)
    last_index = 1
    last_n_ranges = 0
    for index, diff in events:
        frequency[last_n_ranges] += (index - last_index)
        last_n_ranges += diff
        last_index = index
    frequency[0] += (n + 1 - last_index)

    # O(n+m)
    # (A는 오름차순으로 정렬되어 있음.)
    max_s = 0
    n_cases = 1
    for n_ranges, n_elements in reversed(list(enumerate(frequency))):
        # n_ranges개의 구간에 포함된 원소가 n_elements개.
        for i in range(n_elements):
            max_s += n_ranges * A.pop()
        n_cases = mmul(n_cases, MOD_FACTORIAL[n_elements]) # 원소를 배치하는 경우의 수

    stdout.write(f'{max_s} {n_cases}\n')


if __name__ == "__main__":
    init_mod_factorial()
    for t in range(int(stdin.readline())):
        testcase()
