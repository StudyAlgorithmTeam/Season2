from bisect import bisect
from sys import stdin
from sys import stdout


START = 0
END = 1
COUNT = 2


def testcase():
    N = int(stdin.readline())

    meetings = [ tuple(map(int, stdin.readline().split())) for _ in range(N) ]
    meetings.sort()

    dp = [0] * (N+1)

    for i in range(N):
        j = bisect(meetings, meetings[i][END], key=lambda m: m[START])

        for k in range(j, N+1):
            if dp[k] < dp[i] + meetings[i][COUNT]:
                dp[k] = dp[i] + meetings[i][COUNT]

    stdout.write(str(dp[N])+'\n')


if __name__ == '__main__':
    # for t in range(int(stdin.readline())):
    #     testcase()
    testcase()
