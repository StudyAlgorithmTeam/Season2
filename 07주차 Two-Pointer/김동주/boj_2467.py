N = int(input())
liquid = [*map(int, input().split())]

min_res = int(1e12)
min_l = None
min_r = None

l = 0
r = N-1

while l <= r:
    if (val := abs(liquid[l]+liquid[r])) < min_res:
        min_l = l
        min_r = r
        min_res = val

    if abs(l) > abs(r):
        l += 1
    else:
        r -= 1

print(liquid[min_l], liquid[min_r])
