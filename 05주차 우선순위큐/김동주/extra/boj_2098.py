from collections import deque
from sys import stdin
from sys import stdout
from sys import maxsize


W_UNREACHABLE = 0

N = int(stdin.readline())
W = [list(map(int, stdin.readline().split())) for _ in range(N)]
Q = deque(range(N))


def tsp(root: int = None, parent: int = None):
    w = maxsize
    if Q:
        loops = len(Q)
        while loops:
            child = Q.popleft()
            if root is None:
                w = min(tsp(child, child), w)
            elif W[parent][child] != W_UNREACHABLE:
                w = min(tsp(root, child)+W[parent][child], w)
            Q.append(child)
            loops -= 1
    else: # empty queue (visited all nodes)
        child = root
        if W[parent][child] != W_UNREACHABLE:
            w = W[parent][child]
    return w


stdout.write(str(tsp()))
stdout.write('\n')
