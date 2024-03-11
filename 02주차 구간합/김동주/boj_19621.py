from dataclasses import dataclass
from sys import stdin
from sys import stdout


@dataclass(order=True)
class Meeting:
    start: int
    end: int
    capacity: int


N = int(stdin.readline())

meetings = [Meeting(*map(int, stdin.readline().split())) for i in range(N)]
meetings.sort()


def dp(index: int = 0, end: int = -1) -> int:
    """
    end: 선택 된 회의들 중 가장 마지막 회의가 끝나는 시간.
    """
    # 모든 회의를 다 본 경우
    if index == N:
        return 0

    meeting = meetings[index]

    # 마지막 회의와 시간이 겹침. -> pass
    if meeting.start < end:
        return dp(index+1, end)

    # index 번째 미팅을 포함하는 경우 & 포함하지 않는 경우
    excluded = dp(index+1, end)
    included = meeting.capacity + dp(index+1, meeting.end)
    return max(included, excluded)

stdout.write(str(dp()))