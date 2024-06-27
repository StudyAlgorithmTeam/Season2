# 2xN 예쁜 타일링


N, A, B = map(int, input().split())
TA = sorted(map(int, input().split()))
TB = sorted(map(int, input().split()))

ans = 0

if N % 2 == 1:
    ans += TA.pop()
    N -= 1

while N > 0:
    if len(TA) >= 2 and TB:
        if TA[-1]+TA[-2] > TB[-1]:
            ans += TA.pop() + TA.pop()
        else:
            ans += TB.pop()
    elif TB:
        ans += TB.pop()
    else:
        ans += TA.pop() + TA.pop()
    N -= 2

print(ans)
