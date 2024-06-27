T = int(input())
test_list = []
result = []

for _ in range(T):
    test_list.append(list(input()))

for case in test_list:
    count = 0
    for i in case:
        if count < 0:
            break
        else:
            if i == "(":
                count += 1
            else:
                count -= 1
    if count == 0:
        result.append("YES")
    else:
        result.append("NO")


print(*result,sep="\n")