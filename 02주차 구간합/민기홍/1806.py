import sys

input = sys.stdin.readline

N, S = map(int, input().split())    # N:배열 길이, S: 부분합 기준
sequence = tuple(map(int, input().split())) # 길이 N의 수열

L, R = 0, 0 # L: 왼쪽(left) , R: 오른쪽(right)
min_length = 100000 # 부분합의 최소 길이
now_sum = 0 # S와 비교하기 위한 변수(부분합을 저장해놓을 변수)

# 최악의 경우 2n만큼의 시간 소요가 됨.
# 최선의 경우 n만큼의 시간 소요가 됨.
# O(n) 시간복잡도
while True:
    if now_sum < S:
        now_sum += sequence[R]
        R += 1
    elif now_sum >= S:
        min_length = min(min_length, R-L)
        now_sum -= sequence[L]
        L += 1
    if R >= N and now_sum < S:
        break


# 정답 출력
if min_length != 100000:
    print(min_length)
else :  # 수열의 부분합으로 S 이상을 만들지 못할 때
    print(0)