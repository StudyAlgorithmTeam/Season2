edit_string = list(input())

string_count = len(edit_string)
location = string_count    #현재 커서 위치

# 예제 입력 및 검사
M = int(input())

for _ in range(M):
    input_ex = list(input().split())
    if input_ex[0] == "L":
        if location > 0:
            location -= 1
    elif input_ex[0] == "D":
        if location < string_count:
            location += 1
    elif input_ex[0] == "P":
        edit_string.insert(location, input_ex[1])
        location += 1
    elif input_ex[0] == "B":
        if location > 0:
            edit_string.remove(edit_string[location - 1])
            location -= 1

# 결과 출력
print(''.join(edit_string))