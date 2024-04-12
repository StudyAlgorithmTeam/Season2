import collections


N, M = map(int, input().split())
q = collections.deque(range(1,N+1))
ans = 0
for a in map(int, input().split()):
    l = len(q)
    r = 0
    while q[0] != a:
        q.rotate()
        r += 1
        l -= 1
    q.popleft()
    ans += min(l, r)

print(ans)
