N = int(input())
M = int(input())
# N < 200 , M < 1000

city = list(range(N+1))

def find(x): #O(N) ==> O(logN)
    while x != city[x]:
        x = city[x]
    return x

def union(a,b): #O(N) ==> O(logN)
    first = find(a)
    second = find(b)

    if first < second:
        first, second = second, first

    city[first] = second

for i in range(1,N+1): # O(N * M)
    link = list(map(int, input().split()))
    index = 1
    for j in link:
        if j == 1:
            union(i,index)
        index = index + 1

travel = list(map(int,input().split()))

tmp = find(travel[0])
check = True

for i in travel: # O(N)
    if tmp != find(city[i]):
        print("NO")
        check = False
        break

if check:
    print("YES")
