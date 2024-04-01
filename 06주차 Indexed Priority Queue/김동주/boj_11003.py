import collections
import heapq
from sys import stdin
from sys import stdout


HEAP_ELEM_VALUE = 0
HEAP_ELEM_KEY = 1

N, L = map(int, stdin.readline().split())

heap = []
q = collections.deque()

for i, A_i in enumerate(map(int, stdin.readline().split())):
    q.append(A_i)
    heapq.heappush(heap, (A_i, i))
    if i >= L:
        q.popleft()
        while heap[0][HEAP_ELEM_KEY] < i-L+1:
            heapq.heappop(heap)
    stdout.write(str(heap[0][HEAP_ELEM_VALUE])+' ')
