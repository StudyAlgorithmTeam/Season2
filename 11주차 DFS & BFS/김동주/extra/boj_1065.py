# 한수

N = int(input())

is_hansu = [False] * (N+1)
count = 0

for step in range(-9, 10):
    for number in range(1,10):
        # 이 아래 반복문은 N의 자릿수 만큼 수행
        while 1 <= number and number <= N:
            if not is_hansu[number]:
                count += 1

            is_hansu[number] = True

            new_digit = (number % 10) + step
            if not (0 <= new_digit and new_digit <= 9):
                break
            number = 10 * number + new_digit

print(count)
