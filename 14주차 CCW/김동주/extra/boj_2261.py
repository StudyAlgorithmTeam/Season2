# 가장 가까운 두 점

import dataclasses
import math
import sys


@dataclasses.dataclass(order=True)
class Point:
    x: int
    y: int


N = int(sys.stdin.readline())
P = [Point(*map(int, sys.stdin.readline().split())) for i in range(N)]
P.sort()


def find_closest_dist_sqaure(s: int, e: int) -> int:
    if s+16 > e:
        min_d = sys.maxsize
        idx = list(range(s, e+1))
    else:
        mid = (s+e)//2
        dl = find_closest_dist_sqaure(s, mid-1)
        dr = find_closest_dist_sqaure(mid+1, e)
        min_d = min(dl, dr)
        idx = []
        for i in reversed(range(s, mid)):
            if abs(P[i].x-P[mid].x) >= math.sqrt(min_d):
                break
            idx.append(i)
        for i in range(mid, e+1):
            if abs(P[i].x-P[mid].x) >= math.sqrt(min_d):
                break
            idx.append(i)
    for i in range(len(idx)):
        for j in range(i+1, len(idx)):
            if min_d > (d := (P[idx[i]].x-P[idx[j]].x)**2+(P[idx[i]].y-P[idx[j]].y)**2):
                min_d = d
    return min_d


if __name__ == '__main__':
    sys.setrecursionlimit(max(1000, 2*N))
    print(int(find_closest_dist_sqaure(0, N-1)))
