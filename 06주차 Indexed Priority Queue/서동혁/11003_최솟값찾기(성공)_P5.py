from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split()) # 1 <= L <= N <= 5,000,000 => 500만

A = list(map(int, input().split()))

deque_min = deque()

VALUE = 0
INDEX = 1

for i in range(N):
    if(deque_min and deque_min[0][INDEX] + L == i): # deque 안에 원소가 있고, 제일 앞의 원소의 index + L이 i와 같아지면 L 범위를 넘어가므로 popleft
        deque_min.popleft()

    while deque_min and deque_min[-1][VALUE] > A[i]: # deque의 뒤에서부터 A[i] 보다 크면 pop해서 제거 (어차피 필요 없는 숫자임 뒤 숫자에 밀려서)
        deque_min.pop()
    
    deque_min.append((A[i],i)) # value , index 순으로 튜플 만듬 => list 보다 튜플이 메모리 차지 적음

    print(deque_min[0][VALUE], end =' ')