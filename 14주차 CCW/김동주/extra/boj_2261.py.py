# 가장 가까운 두 점

from __future__ import annotations
import sys
import typing


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'{self.x} {self.y}'


MAX_N = 100000
MAX_SIZE = 10000


def dist_square(u: Point, v: Point) -> int:
    return (u.x-v.x)**2 + (u.y-v.y)**2


def solve(points: typing.List[Point], s: int, e: int) -> int:
    if e-s <= 1:
        return sys.maxsize
    if e-s == 2:
        return dist_square(points[s], points[s+1])
    if e-s == 3:
        return min(
            dist_square(points[s], points[s+1]),
            dist_square(points[s], points[s+2]),
            dist_square(points[s+1], points[s+2]),
        )
    m = (s+e)//2
    p = points[m]
    dl = solve(points, s, m)
    dr = solve(points, m+1, e)
    min_d = min(dl, dr)
    min_d_sqrt = min_d ** 0.5 + 1

    points = sorted([points[i] for i in range(s, e) if abs(points[i].x-p.x) < min_d_sqrt], key=lambda p: p.y)
    for i in range(len(points)):
        for j in reversed(range(i)):
            d = dist_square(points[i], points[j])
            dy = abs(points[i].y - points[j].y)
            if dy >= min_d:
                break
            if min_d > d:
                min_d = d
                min_d_sqrt = min_d ** 0.5 + 1
    return min_d


if __name__ == '__main__':
    sys.setrecursionlimit(10*MAX_N)
    N = int(sys.stdin.readline())
    P = sorted([Point(*map(int, sys.stdin.readline().split())) for i in range(N)], key=lambda p: p.x)
    print(solve(P, 0, N))
