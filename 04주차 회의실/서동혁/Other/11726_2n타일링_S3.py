N = int(input()) # 피보나치 수와 관련해서 풀어보기

# DP = [0] * (10007) # 이걸 N+1로 하면 런타임 에러가 뜨네
DP = [0] * 3
DP[1] = 1
DP[2] = 2

for i in range(3,N+1):
    DP[i % 3] = (DP[(i-1) % 3] + DP[(i-2) % 3]) % 10007

print(DP[N % 3])