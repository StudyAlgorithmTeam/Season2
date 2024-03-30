from sys import stdin
from sys import stdout
from sys import setrecursionlimit


MAX_N = int(1e6)

n = int(stdin.readline())
preorder = []
inorder = list(map(int, stdin.readline().split()))
postorder = list(map(int, stdin.readline().split()))


def traverse(in_s: int, in_e: int, post_s: int, post_e: int):
    root = postorder[post_e]

    preorder.append(root)

    ltree_size = inorder.index(root)-in_s
    rtree_size = in_e-in_s-ltree_size

    if ltree_size > 0:
        traverse(in_s, in_s+ltree_size-1, post_s, post_s+ltree_size-1)
    if rtree_size > 0:
        traverse(in_e-rtree_size+1, in_e, post_e-rtree_size, post_e-1)


setrecursionlimit(MAX_N << 1)
traverse(0, n-1, 0, n-1)
stdout.write(' '.join(map(str, preorder))+'\n')
