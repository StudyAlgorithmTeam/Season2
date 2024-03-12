from sys import stdin
from sys import stdout

MAX_L = 5000
MOD = int(1e9+7)


DP = [[0] * (MAX_L+1) for _ in range(MAX_L+1)]

DP[0][0] = 1

for length in range(MAX_L):
    # opn_par : number of opened parenthesis in the sequence
    for opn_par in range(min(length+2, MAX_L)):
        # parenthesis opened.
        DP[length+1][opn_par] = DP[length][opn_par-1]

        # parenthesis closed.
        DP[length+1][opn_par] += DP[length][opn_par+1]

        DP[length+1][opn_par] %= MOD


for t in range(int(stdin.readline())):
    L = int(stdin.readline())
    stdout.write(DP[L][0].__str__()+'\n')
