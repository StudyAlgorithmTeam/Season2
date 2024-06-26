N = int(input())
BASES = {
    False: '01T', # for positives
    True: '0T1', # for negatives
}
digits = []

is_negative = N < 0
if is_negative:
    N *= -1

while N:
    d = N % 3
    digits.append(d)
    N //= 3

digits.append(0)
for i in range(len(digits)-1):
    # handles carry
    digits[i+1] += digits[i] // 3
    digits[i] %= 3
    # converts 2 to -1 by borrowing
    if digits[i] == 2:
        digits[i] = -1
        digits[i+1] += 1
if len(digits) > 1 and digits[-1] == 0:
    digits.pop()
digits.reverse()

# stringify
for i in range(len(digits)):
    digits[i] = BASES[is_negative][digits[i]]

print(''.join(digits))
