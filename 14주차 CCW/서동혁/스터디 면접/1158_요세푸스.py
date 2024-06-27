from collections import deque

N, K = map(int,input().split())

temp = deque(list(range(1,N+1)))
josephus = []

while temp:
    temp.rotate(-K)
    josephus.append(temp.pop())

print(str(josephus).replace('[','<').replace(']','>'))