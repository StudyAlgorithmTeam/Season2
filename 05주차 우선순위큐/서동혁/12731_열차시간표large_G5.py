import heapq
import sys
input = sys.stdin.readline

N = int(input()) # N <= 100

for i in range(N):
    A_Count = 0 
    B_Count = 0
    # 각 테스트 case 들의 A역과 B역의 필요 열차 수

    Interval_Time = int(input()) # 회차시간

    NA, NB = map(int, input().split()) # NA, NB <= 20

    result_A = []
    result_B = []
    # 열차들의 시간을 나타내는 리스트 => 0번째 index = 출발시간, 2번째 index = 도착시간

    for a in range(NA):
        temp_s = input().split(" ")
        temp = ":".join(temp_s)
        temp_s = temp.split(":")
        # ex) 09:00 12:00 => [9 0 12 0] int 리스트로 형 변환

        abc = []
        for b in temp_s:
            abc.append(int(b))
        
        result_A.append(abc)  # extend 함수는 리스트를 그대로 이어 붙임 + 이랑 같은 역할인듯

        result_A[a][0] = result_A[a][0] * 60 + result_A[a][1]
        result_A[a][2] = result_A[a][2] * 60 + result_A[a][3]
        # 분 단위로 출발 시간 및 도착 시간을 환산해 0 2번째 index에 넣음

    result_A.sort(key = lambda x : x[0]) # 출발 시간을 기준으로 정렬
    result_A.append([9999999,9999999]) # 예시 2처럼 B의 시각이 없을 때 index out of range 나오는 것을 방지하기 위해 큰 수를 삽입함

    for a in range(NB):
        temp_s = input().split(" ")
        temp = ":".join(temp_s)
        temp_s = temp.split(":")
        abc = []
        for b in temp_s:
            abc.append(int(b))
        
        result_B.append(abc)

        result_B[a][0] = result_B[a][0] * 60 + result_B[a][1]
        result_B[a][2] = result_B[a][2] * 60 + result_B[a][3]

    result_B.sort(key = lambda x : x[0])
    result_B.append([9999999,9999999])

    A_index = 0
    B_index = 0
    # 스택에서 top을 index로 표시하는것 처럼 정렬된 시간들을 나타내게 함

    tmp_A = [] # B -> A로 출발한 열차가 A에 있는 경우(interval time + b->a 시각의 도착시간)
    tmp_B = [] 

    SCH_DEPARTURE_HOUR = 0
    SCH_DEPARTURE_MIN = 1
    SCH_ARRIVE_HOUR = 2
    SCH_ARRIVE_MIN = 3

    for k in range(NA + NB):
        if result_A[A_index][SCH_DEPARTURE_HOUR] <= result_B[B_index][SCH_DEPARTURE_HOUR]:
            if len(tmp_A) > 0 and tmp_A[0] <= result_A[A_index][SCH_DEPARTURE_HOUR]:
                heapq.heappop(tmp_A)
            else:
                A_Count += 1

            heapq.heappush(tmp_B, result_A[A_index][SCH_ARRIVE_HOUR] + Interval_Time)
            A_index +=1

        else:
            if len(tmp_B) > 0 and tmp_B[SCH_DEPARTURE_HOUR] <= result_B[B_index][SCH_DEPARTURE_HOUR]:
                heapq.heappop(tmp_B)
            else:
                B_Count += 1
            heapq.heappush(tmp_A, result_B[B_index][SCH_ARRIVE_HOUR] + Interval_Time)
            B_index +=1
    

    print("Case #%d: %d %d" % (i+1, A_Count, B_Count))



