import sys
sys.setrecursionlimit(1000000)
# 재귀 깊이 제한 늘리기
# 파이썬은 재귀의 횟수 제한이 있기에 N의 갯수만큼 재귀 깊이를 늘려주어야한다.
# recurrsion error 발생
input = sys.stdin.readline

N, M = map(int,input().split()) 
# N < 1,000,000 , M < 100,000 ==> nlogn 까지

my_set = list(range(N+1))

# 단순 union-find가 아닌 find 경로 압축을 통해 그래프 모양을 바꿔준다.
# https://blogshine.tistory.com/103 참고.
def find(x): # logn
    if my_set[x] != x:
        my_set[x] = find(my_set[x])

    return my_set[x]

def union(a,b): #2logn
    first = find(a)
    second = find(b)

    if first < second:
        first, second = second, first

    my_set[first] = second

for i in range(M):
    decision, fir_set, sec_set = map(int, input().split())

    if decision == 0:
        union(fir_set,sec_set)
    else:
        if find(fir_set) == find(sec_set):
            print("YES")
        else:
            print("NO")

