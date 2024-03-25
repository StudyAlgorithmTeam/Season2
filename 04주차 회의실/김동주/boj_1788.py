MOD = int(1e9)


def testcase():
    n = int(input())

    a, b = 0, 1
    for i in range(abs(n)):
        a, b = b, (a+b)%MOD

    if n == 0:
        print(0)
    elif n < 0 and n % 2 == 0:
        print(-1)
    else:
        print(1)
    print(a)


if __name__ == '__main__':
    # for t in range(int(stdin.readline())):
    #     testcase()
    testcase()
