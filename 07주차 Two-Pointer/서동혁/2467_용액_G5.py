import heapq
import sys
input = sys.stdin.readline

N = int(input()) # N < 100,000

liquid = list(map(int, input().split()))

top = 0
bottom = len(liquid) - 1 #리스트의 마지막 원소

result = [[2000000001,0,0]]

while(top < bottom):
    tmp_sum = liquid[top] + liquid[bottom]
    if tmp_sum == 0:
        heapq.heappush(result, [0,liquid[top],liquid[bottom]])
        break
    elif tmp_sum < 0:
        if abs(tmp_sum) <= result[0][0]:
            heapq.heappop(result)
            heapq.heappush(result, [abs(tmp_sum), liquid[top],liquid[bottom]])
        top = top + 1
    else:
        if abs(tmp_sum) <= result[0][0]:
            heapq.heappop(result)
            heapq.heappush(result, [abs(tmp_sum), liquid[top],liquid[bottom]])
        bottom = bottom - 1
        
print(result[0][1],result[0][2])


#-99 -50 -2 -1 4 98
#음수면 top 가 증가
#양수면 bot 가 감소 

# 1 2 3 4
# 1 과 2 => 점점 증가 스탑

# -9 -6
# 2 5 7 11 14
# 7부터 5 11 비교 -2 -4 2
# 
 