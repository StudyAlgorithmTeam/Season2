# 습격자 초라기

"""
컨셉: 변형 2xN 타일링 계열의 문제처럼 생각해보자.

점화식은 세울 수 있으나, 다음 두 가지에 유의:

1. 초기 조건을 잘 고정하는 것
2. 바텀업 방식으로 풀어야 O(N)에 풀리는 것
"""

import sys
import typing


ROW_UPPER = 0
ROW_LOWER = 1


TILE_X = 0 # 더 이상 인접 타일로 파견 될 수 없는 부대
TILE_L = 1 # 부대의 왼쪽 파견 위치 (오른쪽으로 파견 될 수 있음) (오직 TILE_R 왼쪽에만 올 수 있다.)
TILE_R = 2 # 부대의 오른쪽 파견 위치 (왼쪽으로 파견 될 수 있음) (오직 TILE_L 오른쪽에만 올 수 있다.)

TILE_ALL = (TILE_L, TILE_R, TILE_X)


N: int
W: int
A: typing.List[typing.List[int]]

INF = 100000


class DP:
    """어떤 임의의 한 열에서 나올 수 있는 모든 투입된 소대의 수.

    위의 행의 타일 상태와 아래 행의 타일 상태 조합에 따른 모든 경우의 수를 갖고 있는다.
    """

    def __init__(self) -> None:
        self.N = 3
        self.data = [INF] * (self.N ** 2)

    def clear(self, default=None):
        if default is None:
            default = INF
        for i in range(len(self.data)):
            self.data[i] = default

    def get(self, upper: int, lower: int) -> int:
        """지정한 타일 조합에서 투입되었던 소대 수를 반환.

        upper: 위의 행의 타일 상태
        lower: 아래 행의 타일 상태
        """
        return self.data[self._index(upper, lower)]

    def set(self, upper: int, lower: int, value: int):
        self.data[self._index(upper, lower)] = value

    def _index(self, upper: int, lower: int) -> int:
        return self.N * upper + lower


def is_coverable(y1:int, x1: int, y2: int, x2: int) -> bool:
    """두 칸에 하나의 소대만 투입해도 커버가 되는지 여부를 반환."""
    return A[y1][x1%N] + A[y2][x2%N] <= W


def validate(i: int, upper: int, lower: int) -> bool:
    if upper == TILE_L and not is_coverable(ROW_UPPER, i, ROW_UPPER, (i+1)%N):
        return False
    if lower == TILE_L and not is_coverable(ROW_LOWER, i, ROW_LOWER, (i+1)%N):
        return False
    return True


def expect(i: int, dp: DP, upper: int, lower: int) -> int:
    """upper, lower 타일 조합의 앞에 선행 될 수 있는 경우를 dp에서 모두 찾고,
    그 중 최솟값을 반환한다.
    """
    if not validate(i, upper, lower):
        return INF
    if upper == TILE_R and lower == TILE_R:
        return dp.get(TILE_L, TILE_L)
    elif upper == TILE_R:
        return min(
            dp.get(TILE_L, TILE_R),
            dp.get(TILE_L, TILE_X),
        )
    elif lower == TILE_R:
        return min(
            dp.get(TILE_R, TILE_L),
            dp.get(TILE_X, TILE_L),
        )
    else:
        return min(
            dp.get(TILE_R, TILE_R),
            dp.get(TILE_R, TILE_X),
            dp.get(TILE_X, TILE_R),
            dp.get(TILE_X, TILE_X),
        )


def simulate(i: int, dp: DP, upper: int, lower: int) -> int:
    """이전 열에서의 타일 상태를 담고 있는 dp로 부터 다음 열에서 upper, lower 타일 조합을 만들어 낸다.

    새로운 소대를 투입해야하는 만큼 값을 증가시킨다.
    소대의 수는 오직 TILE_L, 혹은 TILE_X를 할당할 때에만 증가시킨다.
    """
    if upper == TILE_R and lower == TILE_R:
        dw = 0
    elif upper == TILE_R or lower == TILE_R:
        dw = 1
    elif upper == TILE_X and lower == TILE_X and is_coverable(ROW_UPPER, i, ROW_LOWER, i):
        # 하나의 소대를 세로로 배치하는 경우.
        dw = 1
    else:
        dw = 2
    return expect(i, dp, upper, lower) + dw


def solve() -> int:
    if N == 1:
        return 1 if (A[0][0] + A[1][0] <= W) else 2
    answer = sys.maxsize
    curr_dp = DP()
    prev_dp = DP()
    for first_upper in TILE_ALL:
        for first_lower in TILE_ALL:
            # 원형 구조이므로, 계산의 편의를 위해
            # 시작 열의 타일 상태를 고정해두고 사용한다.
            if not validate(0, first_upper, first_lower):
                continue
            # 최초의 열에 값을 세팅한다.
            prev_dp.clear(0)
            curr_dp.clear()
            e = simulate(0, prev_dp, first_upper, first_lower)
            curr_dp.set(first_upper, first_lower, e)
            for i in range(1, N):
                # 1번째 열부터 N번째 열까지 차례로 구한다.
                prev_dp, curr_dp = curr_dp, prev_dp
                curr_dp.clear()
                for upper in TILE_ALL:
                    for lower in TILE_ALL:
                        e = simulate(i, prev_dp, upper, lower)
                        curr_dp.set(upper, lower, e)
            # 마지막 열에서 첫 번째 열로 갈 수 있는 경우만 찾아서 그 최솟값을 구한다.
            e = expect(0, curr_dp, first_upper, first_lower)
            if answer > e:
                answer = e
    return answer


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        N, W = map(int, sys.stdin.readline().split())
        A = [
            list(map(int, sys.stdin.readline().split())),
            list(map(int, sys.stdin.readline().split())),
        ]
        sys.stdout.write(f'{solve()}\n')
