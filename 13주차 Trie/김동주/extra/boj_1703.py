# 생장점

import sys


while True:
    age, *levels = map(int, sys.stdin.readline().split())
    if age == 0:
        break
    splittables = 1
    for i in range(age):
        splittables = (splittables * levels[2*i]) - levels[2*i+1]
    sys.stdout.write(f'{splittables}\n')
