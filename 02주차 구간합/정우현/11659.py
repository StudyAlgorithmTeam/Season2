import sys
input = sys.stdin.readline
#위에 코드를 쓰는이유는
#아래 코드에 Narr에 한번에 배열에 넣는게 아니라 N번 실행되므로
#위에 코드를 쓰면 한번에 배열로 들어간다.
N,M = map(int, input().split())
Narr = list(map(int, input().split()))
result = []
result.append(Narr[0])

for i in range(1,N):
    a = result[i-1] + Narr[i]
    result.append(a)
result.insert(0,0)
for i in range(M):
    x,y = map(int,input().split())
    print(result[y]-result[x-1])
        
