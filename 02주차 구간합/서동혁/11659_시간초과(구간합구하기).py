N, M = map(int, input().split())
#파라미터 없이 문자열.split()하면 띄어쓰기, 엔터를 구분하여 문자열을 나눔
NumList = list(map(int, input().split()))
tempList = [] 

for i in range(M): #O(M)
  temp = list(map(int, input().split()))
  tempList.append(temp)

for i in range(M): # O(M * N)
  start = tempList[i][0]
  end = tempList[i][1]
  sum = 0
  for j in range(start-1,end): #이 부분의 시간 복잡도가 어떻게 되지?
    sum += NumList[j]
  print(sum)
  
  #시간초과 뜨네
  #N , M 이 범위가 100,000 이니까 O(n^2)이면 시간 초과 뜰듯
  #nlogn 찾아봐야될듯 어떻게 줄이지?

  