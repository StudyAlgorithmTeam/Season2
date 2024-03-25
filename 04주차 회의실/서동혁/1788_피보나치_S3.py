n = int(input()) # n < 1,000,000

Fibo_list = [0] * 3 #공간 복잡도 O(1)

#나눗셈은 각각 나누고 더하는것과 다 더하고 나누는게 같다 나누기 연산
#숫자가 매우 커지면 시간복잡도가 뒤지게 올라간다
#나머지 연산을 할 때 A % B 이면 C 언어는 A를 기준으로 나누고 python은 B를 기준으로 나누기에 A가 음수면 B도 음수로 해줘야 일반적인 나머지 연산이 가능하다
#ex) -100 % -90 = -10이 나옴

if n > 0:
    Fibo_list[1] = 1
    for i in range(1, n):
        Fibo_list[(i+1)%3] = (Fibo_list[i%3] + Fibo_list[(i-1)%3])%1000000000
    print(1)
    print(Fibo_list[n%3])

elif n == 0:
    print(0)
    print(0)

else:
    Fibo_list[-1] = 1
    for i in range(0, n+1, -1):
        if Fibo_list[i%3] - Fibo_list[(i-1)%3] > 0:
            Fibo_list[(i-2)%3] = (Fibo_list[i%3] - Fibo_list[(i-1)%3])%1000000000
        else:
            Fibo_list[(i-2)%3] = (Fibo_list[i%3] - Fibo_list[(i-1)%3])%-1000000000
    if Fibo_list[n%3] > 0:
        print(1)
        print(Fibo_list[n%3])
    else:
        print(-1)
        print((-Fibo_list[n%3]))

#이자식 pypy 7204면 7초 아닌가? 왜 시간초과 아니게 뜬거지? 백준에서