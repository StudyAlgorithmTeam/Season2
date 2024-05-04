# Shuffle

n, t = map(int, input().split())
if t % 2 == 0:
    print(input())
else:
    print(' '.join(reversed(input().split())))
