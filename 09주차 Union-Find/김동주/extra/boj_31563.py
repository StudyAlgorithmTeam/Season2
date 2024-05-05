# 수열 회전과 쿼리

import sys


N, Q = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

A_ACC = [0] * N
for i in range(N):
    A_ACC[i] = A_ACC[i-1] + A[i]

s = 0
e = N-1
for i in range(Q):
    cmd, *args = map(int, sys.stdin.readline().split())
    match cmd:
        case 1:
            s = (s - args[0]) % N
            e = (e - args[0]) % N
        case 2:
            s = (s + args[0]) % N
            e = (e + args[0]) % N
        case 3:
            a = (s + args[0] - 1) % N
            b = (s + args[1] - 1) % N
            acc = A_ACC[b] - A_ACC[a] + A[a]
            if a > b:
                acc += A_ACC[N-1]
            sys.stdout.write(f"{acc}\n")
