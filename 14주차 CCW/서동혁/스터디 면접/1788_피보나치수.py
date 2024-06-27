n = int(input()) # n < 1,000,000

Fibo_list = [0] * 3 #공간 복잡도 O(1)

if n > 0:
    Fibo_list[1] = 1
    for i in range(1, n): # 1 1 이면 어케됨??
        Fibo_list[(i+1)%3] = (Fibo_list[i%3] + Fibo_list[(i-1)%3])%1000000000
    print(1)
    print(Fibo_list[n%3]%1000000000)

elif n == 0:
    print(0)
    print(0)

else:
    Fibo_list[-1] = 1
    for i in range(0, n+1, -1):
        if Fibo_list[i%3] - Fibo_list[(i-1)%3] > 0:
            Fibo_list[(i-2)%3] = (Fibo_list[i%3] - Fibo_list[(i-1)%3])%1000000000
        else:
            Fibo_list[(i-2)%3] = (Fibo_list[i%3] - Fibo_list[(i-1)%3])%-1000000000
    if Fibo_list[n%3] > 0:
        print(1)
        print(Fibo_list[n%3])
    else:
        print(-1)
        print((-Fibo_list[n%3]))