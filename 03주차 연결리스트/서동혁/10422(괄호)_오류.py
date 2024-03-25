T = int(input())

for i in range(T):
    L = int(input())
    up_num = 1
    down_num = 1
    if L % 2 != 0:
        print(0)
    else:
        L = L - 2
        for j in range(1, int(L/2)+1):
            up_num = up_num * (L + 1 - j)
            down_num = down_num * j
        num = (up_num /down_num) % 1000000007
        print(num)
