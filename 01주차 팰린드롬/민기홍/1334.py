N = int(input())
N = N+1
S = []

temp = str(N)
for i in range(len(temp)):
    S.append(int(temp[i]))

for i in range(len(S)//2):
    if S[i] != S[len(S)-1-i]:
        if S[i] < S[len(S)-1-i]:
            if S[len(S) - i - 2] < 9:
                S[len(S) - i - 2] = S[len(S) - i - 2] + 1
            else:   #12991, 4995에 대한 반례 해결
                j = 0
                while (S[len(S) - i - 2 - j] + 1) // 10:
                    S[len(S) - i - 2 - j] = 0
                    j = j + 1
                S[len(S) - i - 2 - j] = S[len(S) - i - 2 - j] + 1

        S[len(S)-1-i] = S[i]

for i in range(len(S)):
    print(S[i], end="")
