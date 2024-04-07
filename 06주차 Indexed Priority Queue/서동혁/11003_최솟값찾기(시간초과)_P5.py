import sys
input = sys.stdin.readline
from collections import deque

N, L = map(int, input().split()) # 1 <= L <= N <= 5,000,000 => 500만

A = [(0,0)] # 0번째 index는 value , 1번째 index는 index순서

deque1 = deque() # 덱으로 앞 뒤로 빼는 것 구현하기

for index, value in enumerate(map(int, input().split()), start=1): # value , index 순으로 튜플 만듬 => list 보다 튜플이 메모리 차지 적음
    A.append((value, index))

result = [] # 각 구간들의 최솟값을 저장하는 리스트

deque1.append(A[1][0])
tmp = A[1][1]

for i in range(2, N + 1):
    for j in reversed(deque1): #뒤부터
        if j[0] > A[i][0]:
            deque1.pop() 
    deque1.append(A[i][0])

    tmp = deque1[0][1] # 덱 맨 앞의 value 의 index

    if (tmp + L >= i):
        deque1.popleft() # index가 L 범위를 넘어가면 pop해서 삭제
    result.append(deque1[0][0])
    
print(result)
