# Autocorrelation

from collections import deque
import sys


MIN_X = -100
MIN_R = -100


if __name__ == "__main__":
    while True:
        # n, r 입력 및 종료 조건 검사
        n, r = sys.stdin.readline().split()
        n, r = int(n), float(r)
        if n == 0 and r == 0:
            break

        # 곱해야 할 두 함수 f(x)와 f(x+r)를 각각 f(x), g(x)라고 함.
        # 각 원소는 (x, y) 좌표 쌍을 나타냄.
        f = deque()
        g = deque()
        for i in range(n):
            x, y = map(int, sys.stdin.readline().split())
            f.append((x, y))
            g.append((x+r, y))

        # 구해야 할 값 초기화
        autocorrelation = 0.0

        # 작은 x 좌표부터 꺼내가며 각 때의 y값을 구함.
        x0 = MIN_X + MIN_R - 1 # divide by zero 방지
        f0 = 0.0
        g0 = 0.0
        while f and g:
            # x0 이후로 가장 먼저 나오는 x 좌표 x1을 찾음.
            # 필요하다면, 선형 보간으로 f 혹은 g값을 구함.
            # f(x) = ax+b
            # g(x) = cx+d
            if f[0][0] == g[0][0]:
                x1, f1 = f.popleft()
                x1, g1 = g.popleft()
                a = (f1-f0)/(x1-x0)
                b = f0 - a*x0
                c = (g1-g0)/(x1-x0)
                d = g0 - c*x0
            elif f[0][0] < g[0][0]:
                x1, f1 = f.popleft()
                a = (f1-f0)/(x1-x0)
                b = f0 - a*x0
                c = (g[0][1]-g0)/(g[0][0]-x0)
                d = g0 - c*x0
                g1 = c*x1 + d
            else:
                x1, g1 = g.popleft()
                a = (f[0][1]-f0)/(f[0][0]-x0)
                b = f0 - a*x0
                c = (g1-g0)/(x1-x0)
                d = g0 - c*x0
                f1 = a*x1 + b

            # Online integral calculator로 구한 공식 적용
            # antiderivative of (ax+b)(cx+d) dx is...
            # ... ac(x^3)/3 + (ad+bc)(x^2)/2 + bdx
            # 정적분이므로 양단의 값의 차로 구간 적분 값을 구함 (적분상수는 사라짐)
            Y0 = a*c*(x0**3)/3 + (a*d + b*c)*(x0**2)/2 + b*d*x0
            Y1 = a*c*(x1**3)/3 + (a*d + b*c)*(x1**2)/2 + b*d*x1

            autocorrelation += Y1-Y0

            x0 = x1
            f0 = f1
            g0 = g1

        sys.stdout.write(f"{autocorrelation}\n")
