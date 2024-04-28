import collections

MAX_N = 100000

N, K = map(int, input().split())

dist = [MAX_N] * (2*MAX_N+1)
count = [0] * (2*MAX_N+1)
is_found = False

queue = collections.deque([N])
depth = 0
width = 1
while queue:
    x = queue.popleft()

    if x == K:
        is_found = True

    if dist[x] >= depth:
        if dist[x] > depth:
            count[x] = 0
        dist[x] = depth
        count[x] += 1

        if x < K:
            queue.append(2*x)
            queue.append(x+1)
        if x > 0:
            queue.append(x-1)

    width -= 1
    if width == 0:
        if is_found:
            break
        depth += 1
        width = len(queue)


print(dist[K])
print(count[K])
