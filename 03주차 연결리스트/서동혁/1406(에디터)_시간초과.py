string = list(input()) #문자열을 바로 list로 만드는 법

M = int(input())

index = len(string) #시작 지점은 맨 뒤

for i in range(M): #O(M)
    select = list(input().split()) #O(1)
    if select[0] == 'L':
        if index > 0:
            index = index - 1
    elif select[0] == 'D':
        if index < len(string):
            index = index + 1
    elif select[0] == 'B':
        if index > 0:
            string.pop(index - 1) #O(N)이 되버리네.... O(1)인줄 알았는데
            index = index - 1
    else:
        if index < len(string):
            string.insert(index, select[1]) #O(N)이 되버리네.... O(1)인줄 알았는데
        else:
            string.append(select[1])
        index = index + 1
   
for i in string:
    print(i, end='')