# 돌게임 6


import sys


CHOICES = (1, 3, 4)
PERIOD = 7 # can_win() 함수의 주기


def _can_win(n: int) -> bool:
    """이 함수는 주기함수이다.

    (True False True True True True False) 주기를 반복함
    """
    if n in CHOICES:
        # 나의 한 수로 승리를 쟁취할 수 있다.
        return True
    if n > 0:
        for choice in CHOICES:
            # 당장은 그리디하게 접근: 내 다음 사람이 져야 함.
            if (n-choice) > 0 and not _can_win(n-choice):
                return True
    return False


def can_win(n: int) -> bool:
    n %= PERIOD
    return _can_win(n if n > 0 else PERIOD)


if __name__ == "__main__":
    sys.setrecursionlimit(int(1e6))

    N = int(sys.stdin.readline())

    print('SK' if can_win(N) else 'CY')
