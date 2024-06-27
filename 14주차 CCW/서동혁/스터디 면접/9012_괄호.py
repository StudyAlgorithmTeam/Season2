import sys

N = int(input())

for _ in range(N):
    bracket = []
    tmp = sys.stdin.readline().rstrip()
    check = True

    for i in range(len(tmp)):
        if tmp[i] == '(':
            bracket.append('(')
        else:
            if bracket:
                bracket.pop()
            else:
                check = False
                break
    
    if bracket or not check:
        print("NO")
    else:
        print("YES")    