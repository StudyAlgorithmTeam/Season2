# 과일 탕후루


N = int(input())
X = input().split()

a = 0 # 탕후루 시작 위치
b = 0 # 탕후루 마지막 위치

fruit_counter = dict() # counter
answer = 0

while b < N:
    while b < N and len(fruit_counter) <= 2:
        if X[b] not in fruit_counter:
            if answer < b-a:
                answer = b-a
            fruit_counter[X[b]] = 0
        fruit_counter[X[b]] += 1
        b += 1
    if len(fruit_counter) > 2:
        fruit_counter[X[a]] -= 1
        if fruit_counter[X[a]] == 0:
            del fruit_counter[X[a]]
        a += 1
    if answer < b-a:
        answer = b-a

print(answer)
