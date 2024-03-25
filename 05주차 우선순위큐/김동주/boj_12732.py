from __future__ import annotations
from dataclasses import dataclass
from dataclasses import field
from heapq import heappush
from heapq import heappop
from sys import stdin
from sys import stdout
from typing import List


@dataclass
class Train:
    timestamp: int # minutes
    diff: int

    # override less than operator for comparision
    def __lt__(self, other: Train):
        if self.timestamp == other.timestamp:
            return self.diff > other.diff
        return self.timestamp < other.timestamp


@dataclass
class Station:
    heap: List[Train] = field(default_factory=list) # 대기 중인 열차 스케쥴의 우선순위 큐
    idle: int = field(default=0) # 역에 대기중인 열차 수
    need: int = field(default=0) # 역에서 출발 시켜야 하는 열차 수


def parse_time(x):
    hh, mm = map(int, x.split(":"))
    return hh * 60 + mm


def testcase(tid):
    T = int(stdin.readline())
    NA, NB = map(int, stdin.readline().split())

    a = Station()
    b = Station()

    for _ in range(NA):
        src, dst = stdin.readline().split()
        heappush(a.heap, Train(parse_time(src), -1))
        heappush(b.heap, Train(parse_time(dst)+T, +1))

    for _ in range(NB):
        src, dst = stdin.readline().split()
        heappush(b.heap, Train(parse_time(src), -1))
        heappush(a.heap, Train(parse_time(dst)+T, +1))

    while a.heap and b.heap:
        station = a if a.heap[0].timestamp < b.heap[0].timestamp else b
        station.idle += heappop(station.heap).diff
        if station.idle < 0:
            station.idle = 0
            station.need += 1

    station = a if a.heap else b
    while station.heap:
        station.idle += heappop(station.heap).diff
        if station.idle < 0:
            station.idle = 0
            station.need += 1

    stdout.write(f'Case #{tid}: {a.need} {b.need}')
    stdout.write('\n')


if __name__ == '__main__':
    T = int(stdin.readline())
    for t in range(1, T+1):
        testcase(t)
