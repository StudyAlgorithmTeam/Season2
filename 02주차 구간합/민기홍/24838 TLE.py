import math

result = []
def prefix_func():
    n, m = map(int, input().split())  # n:배열길이 / m:부분합 개수
    A = list(map(int, input().split()))  # A:n개의 원소를 가진 배열
    prefix_index = []  # prefix_sum: 입력한 부분합의 범위 m개가 담긴 리스트
    overlap = [0 for i in range(n)]  # 부분합에서 겹치는 부분
    A.sort()

    total = 0  # 총합의 최대
    counting = 1  # 가능한 경우의 수

    for i in range(m):  # 부분합을 prefix_sum에 담기
        prefix_index.append(list(map(int, input().split())))
        for _ in range(prefix_index[i][0] - 1, prefix_index[i][1]):
            overlap[_] += 1

    for _ in reversed(list(set(overlap))):
        overlap_count = overlap.count(_)  # 겹친 부분 개수
        counting *= (math.factorial(overlap_count)) % int(1e9 + 7)
        if _ > 0:
            for i in range(overlap_count):
                total += _ * A[n - 1]
                if i != overlap_count - 1:
                    n -= 1
            n -= 1

    result.append([total, counting])
    return 0

T = int(input())        # test case 수

for test_case in range(T):
    prefix_func()

for _ in range(T):
    print(result[_][0], end=" ")
    print(result[_][1])

