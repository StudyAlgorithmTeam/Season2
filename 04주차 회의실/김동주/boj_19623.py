from bisect import bisect_left
from sys import stdin
from sys import stdout


START = 0
END = 1
COUNT = 2


def testcase():
    N = int(stdin.readline())

    meetings = [ tuple(map(int, stdin.readline().split())) for _ in range(N) ]
    meetings.sort(key=lambda m: m[END]) # 종료 시간 기준으로 정렬

    dp = [0] * N # i 번째 회의가 끝났을 때, 최대 인원

    for i in range(N):
        dp[i] = meetings[i][COUNT]

        j = bisect_left(meetings, meetings[i][START], lo=0, hi=i, key=lambda m: m[END])

        for k in range(j):
            if dp[i] < dp[k] + meetings[i][COUNT]:
                dp[i] = dp[k] + meetings[i][COUNT]

    stdout.write(str(max(dp))+'\n')


if __name__ == '__main__':
    # for t in range(int(stdin.readline())):
    #     testcase()
    testcase()
