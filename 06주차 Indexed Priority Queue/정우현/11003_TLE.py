import heapq
import sys
input = sys.stdin.readline

N,L = map(int,input().split())
A = list(map(int,input().split()))
A.insert(0,0)
#1부터 비교할려고 앞에 값을 넣어줌

result = []

start=1
end=1
print(A[1],end= ' ')
while start <= N:
    heap_min = []
    if start == end:
        start += 1
        result.append(A[1])
    elif (start - end)+1 > L:
        end += 1
    else:
        for i in range(end,start+1):
            heapq.heappush(heap_min, A[i])
        x = heapq.heappop(heap_min)
        start += 1
        print(x,end=' ')

