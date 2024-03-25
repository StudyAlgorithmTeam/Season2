X = int(input())

s = 0
e = X

while s < e:
    m = (s+e) // 2
    if (m*(m+1)//2) < X:
        s = m+1
    else:
        e = m

level = s-1
offset = level*(level+1)//2

ascend = X-offset
descend = level+1-(ascend-1)

if level & 1 == 0:
    ascend, descend = descend, ascend

print(f'{ascend}/{descend}')
