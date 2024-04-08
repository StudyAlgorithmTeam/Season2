from collections import deque
import sys
input = sys.stdin.readline

N,L = map(int,input().split())
A = list(map(int,input().split()))

temp_A = deque()
count = 1

for i in range(N):
    #맨 앞에 오는 값은 인덱스가 제일 긴데 범위를 넘어가면 pop 
    if temp_A and temp_A[0][1] <=i-L:
        temp_A.popleft()

    #-1을 쓰면 마지막 인덱스 접근 가능
    while temp_A and temp_A[-1][0] > A[i]:
        temp_A.pop()
    #들어가 있는 값은 범위 안에 있는 값인데
    #만약 지금 들어올 값보다 더 크면 pop
    
    temp_A.append((A[i],i))
    print(temp_A[0][0],end=' ')
    
