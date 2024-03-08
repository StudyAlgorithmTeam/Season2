class SegmentTree:
    """구간 트리

    완전 이진 트리에 기반하며, 부모노드는 자식 노드의 구간 값을 가지고 있다.
    트리의 리프 노드에 구간 질의 대상인 배열을 매핑시킬 경우, O(log N) 시간에
    구간 질의를 할 수 있다.

    초기화: O(N log N)
    구간 질의: O(log N)
    갱신: O(log N)

    코드 구현 REF:
    https://www.geeksforgeeks.org/introduction-to-segment-trees-data-structure-and-algorithm-tutorials/
    """

    def __init__(self, array_size: int):
        self.st = [0] * (4 * array_size)
        self.array_size = array_size

    def op(self, a: int, b: int) -> int:
        """구간에 대해 수행할 작업을 정의하는 함수.

        지금은 구간 '합' 트리로 사용하기에 더하기 동작을 수행한다.

        ex) 구간 '곱' 트리의 경우 `a * b`로 변경
        """
        return a + b

    def meaningless_value(self) -> int:
        """구간 외의 값에 대하여 반환 할 값.

        지금은 구간 '합' 트리이므로, 더해져도 의미 없는 숫자인 0을 반환한다.

        ex) 구간 '곱' 트리의 경우 `1`로 변경
        """
        return 0

    def update(self, index: int, value: int):
        """배열의 index 번째 값을 value로 바꾼다."""
        self.__update(index, value, 1, 0, self.array_size-1)

    def __update(self, index: int, value: int, tree_index: int, range_start: int, range_end: int):
        """특정 인덱스의 값을 변경하고, O(log N) 시간에 캐쉬된 구간 값들을 다시 계산함.

        index: 새로 덮어 쓸 값의 배열 상에서의 인덱스
        value: 새로 덮어 쓸 값
        tree_index: 지금 보고 있는 노드의 세그먼트 트리상에서의 인덱스
        range_start: 지금 보고 있는 노드가 커버하는 구간의 시작
        range_end: 지금 보고 있는 노드가 커버하는 구간의 끝
        """
        if range_start == range_end:
            self.st[tree_index] = value
            return
        range_mid = (range_start + range_end) // 2
        if range_start <= index and index <= range_mid:
            self.__update(index, value, self.__lnode_index(tree_index), range_start, range_mid)
        else:
            self.__update(index, value, self.__rnode_index(tree_index), range_mid+1, range_end)
        self.st[tree_index] = self.op(self.st[self.__lnode_index(tree_index)], self.st[self.__rnode_index(tree_index)])

    def query(self, start: int, end: int) -> int:
        """배열의 start 인덱스 부터 end 인덱스 까지의 구간 값을 구한다."""
        return self.__query(start, end, 1, 0, self.array_size-1)

    def __query(self, query_start: int, query_end: int, tree_index: int, range_start: int, range_end: int) -> int:
        """사용자가 질의한 특정 구간의 구간 값을, 사전 계산된 구간 트리에서 탐색하여 O(log N)에 구함.

        query_start: 사용자가 질의한 구간의 시작
        query_end: 사용자가 질의한 구간의 끝
        tree_index: 지금 보고 있는 노드의 세그먼트 트리상에서의 인덱스
        range_start: 지금 보고 있는 노드가 커버하는 구간의 시작
        range_end: 지금 보고 있는 노드가 커버하는 구간의 끝
        """
        if range_end < query_start or query_end < range_start:
            return self.meaningless_value()
        if query_start <= range_start and range_end <= query_end:
            return self.st[tree_index]
        range_mid = (range_start + range_end) // 2
        lnode = self.__query(query_start, query_end, self.__lnode_index(tree_index), range_start, range_mid)
        rnode = self.__query(query_start, query_end, self.__rnode_index(tree_index), range_mid+1, range_end)
        return self.op(lnode, rnode)

    def __lnode_index(self, index: int) -> int:
        return index << 1

    def __rnode_index(self, index: int) -> int:
        return (index << 1) + 1


if __name__ == "__main__":
    import sys
    N, M = map(int, sys.stdin.readline().split())
    # 세그먼트 트리 초기화
    st = SegmentTree(N)
    for index, value in enumerate(map(int, sys.stdin.readline().split())):
        st.update(index, value)
    # 구간 질의 시작
    for _ in range(M):
        i, j = map(int, sys.stdin.readline().split())
        sys.stdout.write(str(st.query(i-1, j-1))+'\n')
