L1 = list(map(int, input().split()))
L2 = list(map(int, input().split()))

# L1을 기준으로 조건 검사
a = L1[0] - L1[2]
b = L1[1] - L1[3]

c = L1[2] - L2[0]
d = L1[3] - L2[1]

e = L1[2] - L2[2]
f = L1[3] - L2[3]

L1_result1 = a * d - b * c
L1_result2 = a * f - b * e

# L2를 기준으로 조건 검사
a = L2[0] - L2[2]
b = L2[1] - L2[3]

c = L2[2] - L1[0]
d = L2[3] - L1[1]

e = L2[2] - L1[2]
f = L2[3] - L1[3]

L2_result1 = a * d - b * c
L2_result2 = a * f - b * e

if L1_result1 * L1_result2 == 0 and L2_result1 * L2_result2 == 0:
    if (min(L1[0], L1[2]) <= max(L2[0], L2[2]) and max(L1[0], L1[2]) >= min(L2[0], L2[2]) and
        min(L1[1], L1[3]) <= max(L2[1], L2[3]) and max(L1[1], L1[3]) >= min(L2[1], L2[3])):
        print(1)
    else:
        print(0)
else:
    if L1_result1 * L1_result2 <= 0 and L2_result1 * L2_result2 <= 0:
        print(1)
    else:
        print(0)
