from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from sys import stdin
from sys import stdout
from typing import Optional


@dataclass
class Node:
    value: str
    lnode: Optional[Node] = field(default=None)
    rnode: Optional[Node] = field(default=None)


@dataclass
class Cursor:
    lnode: Optional[Node] = field(default=None)
    rnode: Optional[Node] = field(default=None)

    def move_left(self):
        # 커서가 문장의 맨 앞이면 무시됨
        if self.lnode is None:
            return
        self.lnode.rnode = self.rnode
        if self.rnode is not None:
            self.rnode.lnode = self.lnode
        self.lnode, self.rnode = self.lnode.lnode, self.lnode

    def move_right(self):
        # 커서가 문장의 맨 뒤이면 무시됨
        if self.rnode is None:
            return
        self.rnode.lnode = self.lnode
        if self.lnode is not None:
            self.lnode.rnode = self.rnode
        self.lnode, self.rnode = self.rnode, self.rnode.rnode

    def insert(self, value: str):
        nnode = Node(value=value, lnode=self.lnode, rnode=self)
        if self.lnode is not None:
            self.lnode.rnode = nnode
        self.lnode = nnode

    def backspace(self):
        # 문장의 맨 앞이면 무시.
        if self.lnode is None:
            return
        dnode = self.lnode
        if self.lnode.lnode is None:
            self.lnode = None
        else:
            self.lnode.lnode.rnode, self.lnode = self, self.lnode.lnode
        del dnode


cursor = Cursor()

for character in stdin.readline().strip():
    cursor.insert(character)

for _ in range(int(stdin.readline())):
    cmd, *args = stdin.readline().strip().split()
    if cmd == 'L':
        cursor.move_left()
        continue
    if cmd == 'D':
        cursor.move_right()
        continue
    if cmd == 'B':
        cursor.backspace()
        continue
    else:
        cursor.insert(args[0])

while cursor.lnode is not None:
    cursor.move_left()

node = cursor.rnode
while node is not None:
    stdout.write(node.value)
    node = node.rnode
stdout.write('\n')
