N, M = map(int, input().split())    # N:수의 개수, M: testcase 횟수
num_list = list(map(int, input().split())) # 크기가 N인 숫자 리스트
test_case = []
perfix_sum = [0]

temp = 0
for _ in range(N):
    temp += num_list[_]
    perfix_sum.append(temp)

for _ in range(M):
    test_case.append(list(map(int, input().split())))

for _ in range(M):
    print(perfix_sum[test_case[_][1]] - perfix_sum[test_case[_][0]-1])
