from sys import stdin
from sys import stdout


def testcase():
    N, M = map(int, stdin.readline().split())
    A = [list(map(int, stdin.readline().split())) for _ in range(N)]
    M, K = map(int, stdin.readline().split())
    B = [list(map(int, stdin.readline().split())) for _ in range(M)]
    C = [[0] * K for _ in range(N)]

    for i in range(N):
        for j in range(K):
            for k in range(M):
                C[i][j] += A[i][k] * B[k][j]
            stdout.write(str(C[i][j]) + ' ')
        stdout.write('\n')



if __name__ == '__main__':
    # for t in range(int(stdin.readline())):
    #     testcase()
    testcase()
