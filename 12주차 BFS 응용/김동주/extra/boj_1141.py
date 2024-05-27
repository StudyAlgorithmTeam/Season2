# 접두사

from __future__ import annotations
from collections import defaultdict
from typing import Set
import sys


class Node:
    def __init__(self) -> None:
        self.word = ''
        self.children = defaultdict(Node)
        self.n_childs = 0

    def __hash__(self) -> int:
        return hash(self.word)

    def add(self, word: str, i: int = 0) -> Node:
        if i == len(word):
            self.word = word
            return self
        else:
            self.n_childs += 1
            return self.children[word[i]].add(word, i+1)


N = int(sys.stdin.readline())

root = Node()
leaf: Set[Node] = set()

for i in range(N):
    word = sys.stdin.readline().strip()
    node = root.add(word)
    leaf.add(node)

count = 0
for node in leaf:
    if node.n_childs == 0:
        count += 1
print(count)
