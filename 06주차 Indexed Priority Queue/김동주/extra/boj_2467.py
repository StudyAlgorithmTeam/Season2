import functools


N = int(input())
liquid = list(map(int, input().split()))
liquid.sort(key=lambda x: abs(x))

ans = (0, int(1e10))

def filter(a, b):
    global ans
    if abs(a + b) < abs(sum(ans)):
        if a < b:
            ans = a, b
        else:
            ans = b, a
    return b

functools.reduce(filter, liquid)
print(*ans)
