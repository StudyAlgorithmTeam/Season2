# 요세푸스 문제

from collections import deque


N, K = map(int, input().split())
q = deque(range(1, N+1))
stack = []

while q:
    q.rotate(-((K-1) % len(q)))
    stack.append(q.popleft())


print('<'+', '.join(map(str, stack))+'>')
