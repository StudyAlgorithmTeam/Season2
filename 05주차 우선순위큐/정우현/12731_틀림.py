import heapq

N = int(input())

result = []
for i in range(N):
    T = int(input())

    heap_a_arr = [] #A역
    heap_b_arr = [] #B역
    countt = [1,0] # 필요 열차 갯수
    arr_ch = 0 # 출발 시간을 저장하는 변수 (a, b 둘 다)
    aorb = 0 # A or B  A역인지 B역인지 확인 => is_True 같은 bool 형태가 더 좋은듯
    a,b = map(int,input().split()) # NA, NB => F2  rename symbol하면 한번에 변경 가능
    arr_count = a + b -1 # 총 시간의 갯수
    for j in range(a):
        nas_str,nae_str = map(str,input().split())
        nas_str = nas_str.replace(":","")
        nae_str = nae_str.replace(":","")
        nas = int(nas_str)
        nae = int(nae_str)
        heap_a_arr.append((nae,nas))
    for k in range(b):
        nbs_str,nbe_str = map(str,input().split())
        nbs_str = nbs_str.replace(":","")
        nbe_str = nbe_str.replace(":","")
        nbs = int(nbs_str)
        nbe = int(nbe_str)
        heap_b_arr.append((nbe,nbs))
    heapq.heapify(heap_a_arr)
    heapq.heapify(heap_b_arr)
    if len(heap_a_arr) == 0:
        result.append(0,(len(heap_b_arr)))
    elif len(heap_b_arr) == 0:
        result.append((len(heap_a_arr),0))
    else:
        k,l = heapq.heappop(heap_a_arr)
        arr_ch = l
        while arr_count:
            if len(heap_a_arr) == 0 and len(heap_b_arr) == 0:
                break
            else:
                if aorb == 1:#1이면 a에서 b로 간다
                    if not heap_a_arr:
                        aorb = 0
                    else:
                        x,y = heapq.heappop(heap_a_arr)
                        #x는 도착시간 y는 출발시간
                        if not arr_ch+T > y:
                            aorb = 0
                            arr_count -= 1
                            arr_ch = x
                        else:
                            countt[0] += 1
                            aorb = 0
                            arr_count -= 1
                            arr_ch = x
                            
                else:
                    if not heap_b_arr:
                        aorb = 1
                    else:
                        x,y = heapq.heappop(heap_b_arr)
                        if not arr_ch+T > y:
                            aorb = 1
                            arr_count -= 1
                            arr_ch = x
                        else:
                            countt[1] += 1
                            aorb = 1
                            arr_count -= 1
                            arr_ch = x
            
        result.append((countt[0],countt[1]))
            
            
for i in range(len(result)):
    x, y = result[i]
    print("Case #{}: {} {}".format(i + 1, x, y))



#예외 상황
#NB 혹은 NA중 하나가 0일 때
#배열이 사라질 때 까지 진행 하므로 전체 카운트를 설정 하나씩 없애주고 따로 배열 빈지 검사
#하나가 비었다면 다음으로 바로 진행
