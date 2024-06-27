import math

A, B, V = map(int, input().split())
# N < 1,000,000,000 => 10억
'''
while(True):
    tmp = tmp + A
    day = day + 1

    if tmp >= V:
        break
    tmp = tmp - B

    # 시간초과가 무조건 뜨는 식 => 0.25초 불가능
'''
day = math.ceil((V - A) / (A - B)) + 1
print(day)