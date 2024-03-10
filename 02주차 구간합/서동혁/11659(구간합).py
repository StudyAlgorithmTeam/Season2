import sys
input = sys.stdin.readline # 이게 없으니까 시간 초과 뜨네 아오 ㅅㅂ

N, M = map(int, input().split())
NumList = list(map(int, input().split()))
partial_List = [0]

temp_Num = 0

#for i in range(M):  ==> tempList라는 공간복잡도와 값을 입력받고 후에 또 이거에 접근하는것을 없앰
#  temp = list(map(int, input().split()))
#  tempList.append(temp)

for i in NumList:
    temp_Num = temp_Num + i
    partial_List.append(temp_Num)

for i in range(M):
    s, e = map(int, input().split())
    temp = partial_List[e] - partial_List[s-1]
    print(temp)


