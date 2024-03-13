from sys import stdin
from sys import stdout
from typing import List


lstack: List[str] = []
rstack: List[str] = [] # reversed로 사용해야 함에 유의


def move_left(*args):
    # 커서가 문장의 맨 앞이면 무시됨
    if not lstack:
        return
    rstack.append(lstack.pop())

def move_right(*args):
    # 커서가 문장의 맨 뒤이면 무시됨
    if not rstack:
        return
    lstack.append(rstack.pop())

def insert(value: str, *args):
    lstack.append(value)

def backspace(*args):
    # 커서가 문장의 맨 앞이면 무시됨
    if not lstack:
        return
    lstack.pop()


lstack = list(stdin.readline().strip())
commands = {
    'L': move_left,
    'D': move_right,
    'B': backspace,
    'P': insert,
}

for _ in range(int(stdin.readline())):
    cmd, *args = stdin.readline().strip().split()
    commands[cmd](*args)

stdout.write(''.join(lstack) + ''.join(reversed(rstack)) + '\n')
