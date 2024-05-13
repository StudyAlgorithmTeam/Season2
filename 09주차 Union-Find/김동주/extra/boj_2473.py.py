# 세 용액

import bisect


INF = int(1e9)+1

N = int(input())
liquid = sorted(map(int, input().split()))


def find_last_liquid(s, e) -> int | None:
    l1, l2 = liquid[s], liquid[e]
    desired_l3 = -(l1+l2) # 이 값에 가장 가까운 원소의 위치를 찾아야 함.
    # s, e와 곂치면 안되므로 lo, hi를 설정하여 탐색범위 조정
    i = bisect.bisect(liquid, desired_l3, lo=s+1, hi=e-1)
    possible_i = [j for j in (i-1, i, i+1) if s < j < e]
    if possible_i:
        return min(possible_i, key=lambda i: abs(desired_l3-liquid[i]))
    return None


ans = [INF, INF, INF]

for s in range(N):
    for e in range(s+1, N):
        m = find_last_liquid(s, e)
        if m is None:
            continue
        if abs(sum(ans)) > abs(liquid[s]+liquid[m]+liquid[e]):
            ans[0] = liquid[s]
            ans[1] = liquid[m]
            ans[2] = liquid[e]

print(*ans)
