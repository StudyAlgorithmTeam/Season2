# 토달기

from collections import defaultdict
from typing import Dict, List
import sys


def can_be_followed_by(word: str, followed_by: str) -> bool:
    if len(word) != len(followed_by)-1:
        return False
    for i in range(len(followed_by)):
        if word == followed_by[:i]+followed_by[i+1:]:
            return True
    return False


def dfs(graph: Dict[int, List[int]], visited: List[bool], root: int) -> int:
    visited[root] = True
    for child in graph[root]:
        dfs(graph, visited, child)


if __name__ == '__main__':
    D, W = sys.stdin.readline().split()
    D = int(D)
    WORDS = []
    for i in range(D):
        word = sys.stdin.readline().strip()
        WORDS.append(word)
    WORDS.sort(key=len)

    graph = defaultdict(list)
    for i in range(D):
        for j in range(D):
            if can_be_followed_by(WORDS[i], WORDS[j]):
                graph[i].append(j)

    visited = [False] * (D+1)
    dfs(graph, visited, WORDS.index(W))

    for i in reversed(range(D)):
        if visited[i]:
            print(WORDS[i])
            break
