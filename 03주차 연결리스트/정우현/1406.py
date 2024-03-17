import sys

stack_l = list(input())
stack_r = []
#스택을 2개 이용한다.
n = int(input())

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "L" and stack_l:
        stack_r.append(stack_l.pop())
        #L은 커서를 왼쪽으로 옮기는 건데 마지막 요소를
        #pop 해서 stack_r에 옮긴다. 
    elif command[0] == "D" and stack_r:
        stack_l.append(stack_r.pop())
        #D는 커서를 오른쪽으로 옮기는 거니까 stack_r에 요소가 있어야 작동
        #stack_r의 마지막 값을 stack_l로 옮긴다.
    elif command[0] == "B" and stack_l:
        stack_l.pop()
        #B는 왼쪽을 단순 삭제 따라서 stack_l에 값이 있다면 pop해주면 된다.
    elif command[0] == "P":
        stack_l.append(command[1])
        #P는 문자 추가인데 단순히 stack_l에 값을 넣어주면 된다.

print("".join(stack_l + list(reversed(stack_r))))
#마지막으로 왼쪽과 오른쪽을 합쳐주면 전체 결과가 나온다.
