from sys import stdin
from sys import stdout


def testcase():
    N = int(stdin.readline())
    X = []
    Y = []
    for n in range(N):
        x, y = map(float, stdin.readline().split())
        X.append(x)
        Y.append(y)

    # https://www.mathopenref.com/coordpolygonarea2.html
    # Algorithm to find the area of a polygon
    area = 0
    for i in range(N):
        area += (X[i-1]+X[i]) * (Y[i-1]-Y[i])
    area /= 2

    stdout.write('{:.1f}\n'.format(abs(area), 2))



if __name__ == '__main__':
    # for t in range(int(stdin.readline())):
    #     testcase()
    testcase()
