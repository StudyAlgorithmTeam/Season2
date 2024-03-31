import heapq
import sys
input = sys.stdin.readline

N = int(input())

A_Time = []
B_Time = []

for i in range(N): # N <= 100
    A_Count = 0
    B_Count = 0

    Interval_Time = int(input())
    NA, NB = map(int, input().split())

    result_A = []
    result_B = []

    # NA, NB <= 20
    for a in range(NA):
        temp_s = input().split(" ")
        temp = ":".join(temp_s)
        temp_s = temp.split(":")
        abc = []
        for b in temp_s:
            abc.append(int(b))
        
        result_A.append(abc)  # extend는 그냥 그대로 붙이는거네

        result_A[a][0] = result_A[a][0] * 60 + result_A[a][1]
        result_A[a][2] = result_A[a][2] * 60 + result_A[a][3]

    result_A.sort(key = lambda x : x[0])
    result_A.append([9999999,9999999])

    for a in range(NB):
        temp_s = input().split(" ")
        temp = ":".join(temp_s)
        temp_s = temp.split(":")
        abc = []
        for b in temp_s:
            abc.append(int(b))
        
        result_B.append(abc)  # extend?? 리스트가 두개씩 나오는데 

        result_B[a][0] = result_B[a][0] * 60 + result_B[a][1]
        result_B[a][2] = result_B[a][2] * 60 + result_B[a][3]

    result_B.sort(key = lambda x : x[0])
    result_B.append([9999999,9999999])

    A_index = 0
    B_index = 0
    tmp_A = []
    tmp_B = []

    for k in range(NA + NB):
        if result_A[A_index][0] <= result_B[B_index][0]: #index에러 해결하기 위해 마지막에 99999추가하자
            if len(tmp_A) > 0 and tmp_A[0] <= result_A[A_index][0]:
                heapq.heappop(tmp_A)
                heapq.heappush(tmp_B, result_A[A_index][2] + Interval_Time)
            else:
                heapq.heappush(tmp_B, result_A[A_index][2] + Interval_Time)
                A_Count += 1
            A_index +=1

        else:
            if len(tmp_B) > 0 and tmp_B[0] <= result_B[B_index][0]:
                heapq.heappop(tmp_B)
                heapq.heappush(tmp_A, result_B[B_index][2] + Interval_Time)
            else:
                heapq.heappush(tmp_A, result_B[B_index][2] + Interval_Time)
                B_Count += 1
            B_index +=1
    

    print("Case #%d: %d %d" % (i+1, A_Count, B_Count))