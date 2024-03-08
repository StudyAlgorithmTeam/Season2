pelin = int(input())
pelin = pelin + 1
#1을 더하고 시작하면 홀 짝이 확실히 정해지고 시작 ex)9999
str_pel = str(pelin)

list1 = list(map(int,list(str(pelin))))
num = len(list1)

if(len(list1) % 2 == 0):
  front = str_pel[0:int((num/2))]
  rev_front = int(front[::-1])
  back = int(str_pel[int(num/2):])
  if(rev_front >= back):
    print(int(front + str(rev_front + 1)))
  else:
    temp_front = int(front)+1
    temp_rev_front = int(str(temp_front)[::-1])
    print(int(str(temp_front) + str(temp_rev_front)))
else:
  front = str_pel[0:int((num-1)/2)]
  rev_front = int(front[::-1])
  back = int(str_pel[int((num-1)/2)+1:])
  if(rev_front < back):
    if(list1[int((num-1)/2)]==9):
      temp_front = int(front) + 1
      temp_rev_front = int(str(temp_front)[::-1])
      list1[int((num-1)/2)] = 0
      print(int(str(temp_front) + '0' + str(temp_rev_front)))
    else:
      list1[int((num-1)/2)] = list1[int((num-1)/2)] + 1
      print(int(front + str(list1[int((num-1)/2)]) + str(rev_front)))
  elif(rev_front >= back):
    print(int(front + str(list1[int((num-1)/2)]) + str(rev_front)))