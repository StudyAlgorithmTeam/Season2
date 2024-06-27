import sys
input = sys.stdin.readline

N,K = map(int, input().split())

N_arr = [1]*N
KK = K
result = []

while len(result) < N:
    if KK <= N:
        if N_arr[KK-1] == 1:
            N_arr[KK-1] = 0
            result.append(KK)
        KK += K
    else:
        KK = KK - N
        if N_arr[KK-1] == 1:
            N_arr[KK-1] = 0
            result.append(KK)

print("<",end="")
print(*result,sep=", ",end="")
print(">")

