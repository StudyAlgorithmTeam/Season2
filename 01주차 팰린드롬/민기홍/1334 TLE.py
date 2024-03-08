N = int(input())
S = str(N+1)
def palindrom(S):
    if S[0:] == S[0:][::-1]:
        return 0
    return 1

while palindrom(S):
    N = N+1
    S = str(N)
print(S)