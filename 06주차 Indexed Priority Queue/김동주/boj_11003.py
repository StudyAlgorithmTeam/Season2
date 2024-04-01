from sys import stdin
from sys import stdout


HEAP_ELEM_VALUE = 0
HEAP_ELEM_KEY = 1

heap = []
index = []


def _siftdown(startpos, pos):
    newitem = heap[pos]
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            index[parent[HEAP_ELEM_KEY]] = pos
            pos = parentpos
            continue
        break
    heap[pos] = newitem
    index[newitem[HEAP_ELEM_KEY]] = pos


def _siftup(pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        child = heap[childpos]
        heap[pos] = child
        index[child[HEAP_ELEM_KEY]] = pos
        pos = childpos
        childpos = 2*pos + 1
    heap[pos] = newitem
    index[newitem[HEAP_ELEM_KEY]] = pos
    _siftdown(startpos, pos)


N, L = map(int, stdin.readline().split())

for i, A_i in enumerate(map(int, stdin.readline().split())):
    # remove oldest data to maintain heap L-sized.
    if i >= L:
        pos = index[i-L]
        heap[pos], heap[-1] = heap[-1], heap[pos]
        index[heap[pos][HEAP_ELEM_KEY]] = pos
        index[heap[-1][HEAP_ELEM_KEY]] = None
        if pos < L:
            heap.pop()
        _siftdown(pos, len(heap)-1)
        _siftup(pos-1)

    # add new element
    heap.append((A_i, i))
    index.append(len(heap)-1)
    _siftdown(0, len(heap)-1)

    # construct answer
    stdout.write(str(heap[0][HEAP_ELEM_VALUE]))
    stdout.write(' ')
