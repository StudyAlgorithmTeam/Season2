import heapq
import sys


N = int(sys.stdin.readline())
min_heap = []
max_heap = []

for i in range(N):
    n = int(sys.stdin.readline())
    heapq.heappush(min_heap, n)

    if len(max_heap) < len(min_heap):
        n = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -n)

    if max_heap and min_heap and -max_heap[0] > min_heap[0]:
        min_top = heapq.heappop(min_heap)
        max_top = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, max_top)
        heapq.heappush(max_heap, -min_top)

    sys.stdout.write(f'{-max_heap[0]}\n')
