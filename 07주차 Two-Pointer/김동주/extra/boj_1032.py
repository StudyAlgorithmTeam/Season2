import sys
import functools


def filter(s1: str, s2: str) -> str:
    s = ''
    for c1, c2 in zip(s1, s2):
        s += c1 if c1 == c2 else '?'
    return s



sys.stdout.write(functools.reduce(filter, sys.stdin.readlines()[1:]))
