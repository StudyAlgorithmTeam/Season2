# 돌아온 똥게임

import heapq
import sys


N, D = map(int, sys.stdin.readline().split())

monsters = []
equipments = []

for i in range(N):
    a, x = map(int, sys.stdin.readline().split())
    if a == 1:
        heapq.heappush(monsters, x)
    else:
        heapq.heappush(equipments, x)

while monsters and (D > monsters[0] or equipments):
    while monsters and D > monsters[0]:
        D += heapq.heappop(monsters)
    while monsters and D <= monsters[0] and equipments:
        D *= heapq.heappop(equipments)

print(N - len(monsters))
