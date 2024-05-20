# 단어 나누기 S5

S = input()
N = len(S)

ans = 'z' * N
for i in range(N-2):
    for j in range(i+1, N-1):
        s = S[i::-1]+S[j:i:-1]+S[:j:-1]
        if ans > s:
            ans = s

print(ans)
