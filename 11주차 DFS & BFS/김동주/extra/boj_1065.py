# 한수


N = int(input())


is_hansu = [False] * (N+1)

for begin in range(1,10):
    for step in range(-9, 10):
        number = begin
        while True:
            if not (1 <= number and number <= N):
                break

            is_hansu[number] = True

            new_digit = (number % 10) + step
            if not (0 <= new_digit and new_digit <= 9):
                break
            number = 10 * number + new_digit

count = 0
for i in range(1, N+1):
    if is_hansu[i]:
        count += 1

print(count)
