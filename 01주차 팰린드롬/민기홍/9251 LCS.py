s1 = input()
s2 = input()
L1 = []
L2 = []
maximum1 = 0
maximum2 = 0
now = 0

for _ in range(len(s1)):
    L1.append(s1[_])
for _ in range(len(s2)):
    L2.append(s2[_])

for i in range(len(L1)):
    for j in range(now, len(L2)):
        if L1[i] == L2[j]:
            maximum1 += 1
            now = j
            break
now = 0

for i in range(len(L2)):
    for j in range(now, len(L1)):
        if L2[i] == L1[j]:
            maximum2 += 1
            now = j
            break

maximum = max(maximum1, maximum2)

print(maximum)