n = int(input())

Fibo = [0] * (int(abs(n))+1) # 메모리 초과
Fibo[0] = 0

if n > 0:
    Fibo[1] = 1
    for i in range(2, n+1):
        Fibo[i] = Fibo[i-1] + Fibo[i-2]
    print(1)
    print(Fibo[n])

elif n == 0:
    print(0)
    print(0)

else:
    Fibo[-1] = 1
    for i in range(0, n+1, -1):
        Fibo[i-2] = Fibo[i] - Fibo[i-1]
    if Fibo[n] > 0:
        print(1)
        print(Fibo[n])
    elif Fibo[n] < 0:
        print(-1)
        print(-Fibo[n])
    else:
        print(0)
        print(0)