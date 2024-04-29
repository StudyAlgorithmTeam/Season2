V, E = map(int, input().split())
# 1 <= V <= 10,000 , 1 <= E <= 100,000
mst = []

for _ in range(E): # O(N)
    edge = list(map(int, input().split()))
    mst.append(edge)

mst.sort(key = lambda x : x[2]) # 가중치가 작은 것으로 정렬

mst_set = {mst[0][0], mst[0][1]}

sum = mst[0][2]

for i in range(1,E):
    if mst[i][0] in mst_set and mst[i][1] in mst_set: #cycle이 나오는 경우 넘기기
        continue
    else:
        mst_set.add(mst[i][0])
        mst_set.add(mst[i][1])
        sum = sum + mst[i][2]
    
    if len(mst_set) == V:
        break
print(sum)