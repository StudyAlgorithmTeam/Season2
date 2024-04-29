# 최솟값과 최댓값

from typing import *
import sys


class SegmentTree:
    def __init__(self, size: int, key: Callable[[int, int], int], na: int) -> None:
        self.size = size
        self.tree = [na] * (size << 2)
        self.na = na # 결측치 대채 값
        self.key = key # 부모 노드를 결정하기 위한 함수

    def update(self, index: int, value: int):
        # 1. index 번째 값을 가져야하는 노드의 위치를 이진트리에서 특정함. O(log N)
        node = 0
        start, end = 0, self.size-1
        while start < end:
            mid = (start+end)//2
            if index <= mid:
                end = mid
                node = 2*(node+1)-1 # left
            else:
                start = mid+1
                node = 2*(node+1) # right
        # 2. 값을 갱신함. O(1)
        self.tree[node] = value
        # 3. 구간 트리의 성질을 유지시키기 위해 부모 노드들의 값을 갱신함. O(log N)
        while (node := ((node+1)//2)-1) >= 0: # goes to parent
            lnode = 2*(node+1)-1
            rnode = 2*(node+1)
            self.tree[node] = self.key(self.tree[lnode], self.tree[rnode])

    def query(self, start: int, end: int) -> int:
        return self._query(start, end, 0, 0, self.size-1)

    def _query(self, START: int, END: int, node: int, start: int, end: int) -> int:
        # 1. 탐색 중인 범위(start, end)가 탐색 해야할 범위(START, END)에 포함되면, 구간 대표값만 반환.
        if START <= start and end <= END:
            return self.tree[node]
        # 2. 탐색 중인 범위(start, end)가 탐색 해야할 범위(START, END)를 벗어났으면, 결측치 대채값을 반환 (정답에 영향을 안 주는 수)
        if end < START or END < start:
            return self.na
        # 3. 분할 정복하여 구간 대표값을 찾아 내려감. O(log N)
        lnode = 2*(node+1)-1
        rnode = 2*(node+1)
        mid = (start+end)//2
        return self.key(
            self._query(START, END, lnode, start, mid),
            self._query(START, END, rnode, mid+1, end),
        )


N: int
M: int
min_segtree: SegmentTree
max_segtree: SegmentTree


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    min_segtree = SegmentTree(N+1, key=min, na=sys.maxsize)
    max_segtree = SegmentTree(N+1, key=max, na=0)

    for i in range(1, N+1):
        num = int(sys.stdin.readline())
        min_segtree.update(i, num)
        max_segtree.update(i, num)

    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        sys.stdout.write(f"{min_segtree.query(a, b)} {max_segtree.query(a, b)}\n")