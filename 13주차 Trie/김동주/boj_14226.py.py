# 접두사 찾기

import sys
from collections import defaultdict


class Trie:
    def __init__(self) -> None:
        self.children = defaultdict(Trie)

    def add(self, word: str):
        if len(word) == 0:
            return
        self.children[word[0]].add(word[1:])

    def is_prefix(self, word: str) -> bool:
        if len(word) == 0:
            return True
        return word[0] in self.children and self.children[word[0]].is_prefix(word[1:])


if __name__ == '__main__':
    root = Trie()
    N, M = map(int, sys.stdin.readline().split())
    for i in range(N):
        root.add(sys.stdin.readline().strip())
    ans = 0
    for i in range(M):
        if root.is_prefix(sys.stdin.readline().strip()):
            ans += 1
    print(ans)
