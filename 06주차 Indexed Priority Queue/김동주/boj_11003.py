import heapq
from sys import stdin
from sys import stdout

N, L = map(int, stdin.readline().split())
heap = []

# 원소의 인덱스가 곧 삽입된 시간이라고 하는 것이 메인 컨셉
for i, A_i in enumerate(map(int, stdin.readline().split())):
    heapq.heappush(heap, (A_i, i)) # (원소의 값, 삽입된 시간)
    while heap[0][1] < (i-L+1): # 너무 오래전에 삽입된 것이면 유효하지 않으므로 제거
        heapq.heappop(heap)
    stdout.write(str(heap[0][0])+' ')
