import sys
input= sys.stdin.readline

N = int(input()) # N <100,000

Member_list = [[0,0,0]]

for i in range(N):
    Member_list.append(list(map(int, input().split())))

Member_list.sort(key= lambda x : (x[1],x[0])) #끝나는 시간을 기준으로 정렬
#시간 복잡도가 어떻게 되는거지?

DP = [0] * (N + 1) #공간복잡도 O(N)

for i in range(N,0,-1): # O(N*N)???????? ==> 이걸 줄여야할 것 같은 느낌적인 느낌느낌 O(N!)인가? n-1 ,n-2 , n-3 이런느낌으로?
    for j in range(i-1,0,-1):
        if Member_list[i][0] >= Member_list[j][1]: #후 순번 회의의 시간시간이 전 순번의 끝나는 시간보다 빠른경우
            DP[i] = j
            break

M = [0] * (N+1)

'''def OPT(num): #함수의 시간복잡도는 어떻게 구함??
    if num == 0:
        return 0
    
    if(M[num] !=0):
        return M[num]

    M[num] = max(OPT(DP[num]) + Member_list[num][2], OPT(num-1)) 
    return M[num] '''

M = [0]*(N+1)

for i in range(1, N+1):
    M[i] = max(M[DP[i]] + Member_list[i][2] , M[i - 1])

max = 0

for i in M: #O(N)
    if i >= max:
        max = i

print(max)