from collections import deque
from sys import stdin
from sys import stdout


def testcase():
    N = int(stdin.readline())

    meetings = [ tuple(map(int, stdin.readline().split())) for _ in range(N) ]
    meetings.sort()

    q = deque([(0, 0, None)]) # (회의가 끝난 시간, 누적 인원 수, 파기 시간)

    for s, e, c in meetings:
        for _ in range(len(q)):
            q_end, q_cnt, q_exp = q.popleft()

            if q_exp is not None and q_exp < s:
                continue

            # 이번 회의를 진행 할 경우:
            if q_end <= s:
                q.append((e, q_cnt+c, None))

            if q_exp is None and q_end < e:
                q.append((q_end, q_cnt, e))
            else:
                q.append((q_end, q_cnt, q_exp))
        pass

    max_cnt = 0
    while q:
        cnt = q.pop()[1]
        if cnt > max_cnt:
            max_cnt = cnt

    stdout.write(str(max_cnt)+'\n')


if __name__ == '__main__':
    # for t in range(int(stdin.readline())):
    #     testcase()
    testcase()
