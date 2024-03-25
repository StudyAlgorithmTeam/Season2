from queue import Queue

T = int(input())    # 테스트 케이스
L = []
result = []    # 각 길이별 올바른 괄호문 수

for _ in range(2, 5001, 2):


# '''
# # 괄호 문자열 길이 L
# for _ in range(T):
#     L.append(int(input()))
#
# ## 아이디어: 큐를 쓰자!
# que = Queue()
#
# # 괄호 문자열이 맞는지의 여부 확인 함수
#
# # 홀수일 때는 0개
# for i in range(T):
#     if L[i]%2 != 0:
#         print(0)
#     else:
#         print(result[L[i]])
# '''
