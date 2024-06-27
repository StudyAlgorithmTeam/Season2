# 동혁 피자


import math
import sys


t = 0
while True:
    t += 1
    r, *wl = map(int, sys.stdin.readline().split())
    if r == 0:
        break
    if 2*r >= math.hypot(*wl):
        sys.stdout.write(f'Pizza {t} fits on the table.\n')
    else:
        sys.stdout.write(f'Pizza {t} does not fit on the table.\n')
