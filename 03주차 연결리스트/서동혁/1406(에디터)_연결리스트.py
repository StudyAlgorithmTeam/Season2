
import sys
input= sys.stdin.readline
list1 = list(input().strip()) #문자열을 바로 list로 만드는 법


M = int(input())

list2 = []
# 커서를 기준으로 list1 과 list2로 나눔 시간 복잡도를 더 줄이기 위해 list2는 마지막에 역순으로 꺼냄
for i in range(M): #O(M)
    select = list(input().split()) #O(1)
    if select[0] == 'L':
        if len(list1) > 0:
            list2.append(list1.pop()) 
#L ==> 커서가 왼쪽을 이동이므로 list1의 마지막 원소를 pop해 list2로 append 하면 커서 이동 효과가 가능하다           
    elif select[0] == 'D':
        if len(list2) > 0:
            list1.append(list2.pop())
#D ==> 커서가 오른쪽으로 이동이므로 list2의 마지막 원소를 pop해 list1으로 append 하면 커서 이동 효과가 가능하다
    elif select[0] == 'B':
        if len(list1) > 0:
            list1.pop()
#B ==> 커서가 왼쪽을 기준으로 삭제시켜야 하므로 list1의 마지막 원소를 pop하면 된다.            
    else:
        list1.append(select[1])
#P ==> 커서 왼쪽 기준으로 추가시켜야 하므로 list1에 append하면 된다. 

list2.reverse()
print(''.join(list1) + ''.join(list2))
# print(''.join(list1)) 이렇게도 가능
    
#pypy로는 실행되는데 python으로는 시간초과가 뜸
    
"""list2.reverse() 
Full_list = list1 + list2 # list1 + list2.reverse() 하면 reverse 반환이 none이라서 list + none으로 오류가 뜸
for i in Full_list:
    print(i, end='') """