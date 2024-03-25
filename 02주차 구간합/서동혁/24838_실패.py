T = int(input()) # n * m => 10000000000

MOD = int(1e9 + 7)

for t in range(T):
    n, m = map(int, input().split())
    A_list = list(map(int, input().split()))
    A_list.sort()

    count_list =[0]*(n+1)

    temp_list = []
    for i in range(m):
        start, end = map(int, input().split())
        for j in range(start, end+1):
            count_list[j] = count_list[j] + 1

    count_list.sort()
    
    max = 0
    for i in range(n):
        max = max + count_list[-i-1] * A_list[-i-1]

    count = 0
    tmp = 1
    tmp_mul = 1

    for i in range(1,n+1):
        if count_list[i] != 0:
            if tmp == count_list[i]:
                count = count + 1
                if i == n:
                    tmp_mul = (tmp_mul * count) % MOD
            else:
                tmp = count_list[i]
                tmp_mul = (tmp_mul * count) % MOD
                count = 1
    tmp_mul = tmp_mul % MOD
    print(max,tmp_mul)