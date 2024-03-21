from sys import stdin
from sys import stdout


MAX_N = 100
MAX_C = 100

MAX_TOTAL_COST = MAX_N * MAX_C


def testcase():
    N, M = map(int, stdin.readline().split())
    m = list(map(int, stdin.readline().split()))
    c = list(map(int, stdin.readline().split()))

    # dp[cost]: cost의 비용으로 얻을 수 있는 메모리의 최대 크기
    dp = [0] * (MAX_TOTAL_COST+1)

    for i in range(N):
        dp_prev = dp.copy()
        for cost in range(MAX_TOTAL_COST-c[i]+1):
            if dp[cost+c[i]] < dp_prev[cost] + m[i]:
                dp[cost+c[i]] = dp_prev[cost] + m[i]

    for cost, memory in enumerate(dp):
        if memory >= M:
            stdout.write(str(cost)+'\n')
            break


if __name__ == '__main__':
    # for t in range(int(stdin.readline())):
    #     testcase()
    testcase()
