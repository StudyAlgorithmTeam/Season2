import sys


INF = int(1e9)
N, M = map(int, sys.stdin.readline().split())
PARTY = [0] * M

KNOWS_TRUTH = 0

for person_id in map(int, sys.stdin.readline().split()[1:]):
    KNOWS_TRUTH |= 1 << person_id

for party_id in range(M):
    for person_id in map(int, sys.stdin.readline().split()[1:]):
        PARTY[party_id] |= 1 << person_id


def dp(party_id: int, heard_truth: int, heard_exaggrated: int) -> int:
    if party_id >= M:
        return 0
    # 진실된 이야기를 하는 경우
    if heard_exaggrated & PARTY[party_id]:
        tells_truth = -INF
    else:
        tells_truth = dp(party_id+1, heard_truth | PARTY[party_id], heard_exaggrated)
    # 과장된 이야기를 하는 경우
    if heard_truth & PARTY[party_id]:
        tells_exaggrated = -INF
    else:
        tells_exaggrated = 1 + dp(party_id+1, heard_truth, heard_exaggrated | PARTY[party_id])

    return max(tells_truth, tells_exaggrated)


sys.stdout.write(f'{dp(0, KNOWS_TRUTH, 0)}\n')
