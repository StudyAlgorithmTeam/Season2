import sys

input = sys.stdin.readline

N = int(input())
timeline = []

max_people = 0

for _ in range(N):
    s, e, cost = map(int, input().split())
    timeline.append([e, s, cost])

timeline.sort(reverse=True)

# 아이디어: 전부 조사

def meeting(timeline, i, s, people: int) -> int:    # i: index
    if i == N:
        return people
    else:
        if s >= timeline[i][0]:
            return max(meeting(timeline, i + 1, timeline[i][1], people + timeline[i][2]),meeting(timeline, i + 1, s, people))
        else:
            return meeting(timeline, i + 1, s, people)

for i in range(N):
    max_people = meeting(timeline, i, timeline[0][0], max_people)

print(max_people)