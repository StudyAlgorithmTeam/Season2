N = int(input())
N_arr = list(map(int,input().split()))

start = 0 
end = N-1
temp = [2000000001,0,0]
while start < end:
    x = N_arr[start] + N_arr[end]
    if abs(x) < abs(temp[0]):
        temp[0] = x
        temp[1] = N_arr[start]
        temp[2] = N_arr[end]
    if x == 0:
        break
    elif x < 0:
        start += 1
    else:
        end -= 1


print(temp[1], temp[2])
#temp에는 가장 작은 값이 계속 들어간다.
#처음 값은 가장 큰 값을 넣어준다.
1 2 3 4 5 