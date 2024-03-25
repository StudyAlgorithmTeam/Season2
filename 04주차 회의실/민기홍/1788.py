F = [0, 1]          # 피보나치 수열 F(0), F(1) 초기화
def fibo(F, input_n):   # 필요한 만큼만 피보나치 수열 원소 생성
    for n in range(2, input_n+1):
        F.append((F[n-1] + F[n-2])%int(1e9))

# 입력 받기
n = int(input())

# 피보나치 수열 생성~
fibo(F, abs(n))

# 출력을 위한 검사
if n > 0:               # n > 0
    print(1)
    print(F[n])
elif n == 0:            # n = 0
    print(0)
    print(F[n])
else:                   # n < 0
    if n%2 == 0:        # n 절댓값이 음수면 F(n) < 0
        print(-1)
    else:               # n 절댓값이 양수면 F(n) > 0
        print(1)
    print(F[-n])
