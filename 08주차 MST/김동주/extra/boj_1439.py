S = input().strip()

n_chunks = 1
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        n_chunks += 1

print(n_chunks//2)