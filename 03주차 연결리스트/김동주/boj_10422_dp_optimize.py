from sys import stdin
from sys import stdout

MAX_L = 5000
MOD = int(1e9+7)


# memoize[i] : 길이가 i인 서로 다른 올바른 괄호 문자열의 개수
memoize = [0] * (MAX_L+1)

# dp[i] : i 개의 괄호가 안 닫히고 열려 있을 때
#         나올 수 있는 올바른 괄호 부분 문자열의 개수.
# 마지막 한 칸은 zero-padding
prev_dp = [0] * (MAX_L+2)
dp = [0] * (MAX_L+2)

memoize[0] = dp[0] = 1
for length in range(1, MAX_L+1):
    dp, prev_dp = prev_dp, dp

    for unclosed_parenthesis in range(length+1):
        dp[unclosed_parenthesis] = (prev_dp[unclosed_parenthesis-1] + prev_dp[unclosed_parenthesis+1]) % MOD

    memoize[length] = dp[0] # 모든 괄호가 닫힌, 올바른 괄호 문자열인 것의 개수


for t in range(int(stdin.readline())):
    L = int(stdin.readline())
    stdout.write(memoize[L].__str__()+'\n')
