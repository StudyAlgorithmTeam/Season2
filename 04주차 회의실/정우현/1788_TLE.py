import sys
input = sys.stdin.readline

def fibonaci(i):
    farr = [0,1]
    for j in range(1,i):
        x = farr.pop(0) + farr[0]
        #여기 부분에서 모듈러 연산을 한면 된다
        farr.append(x)
    return(farr[1]) 
#Big Integer - int longlong을 넘어가는 숫자가 되면 처리를 못한다. 문자열로 만들거나(BCD) 오버플로우가 나는 곳을 기준으로 배열을 나누는 식으로 한다.  
n = int(input())


if n == 0:
    print(0)
    print(0)

elif n == 1:
    print(0)
    print(1)

elif n < 0:
    n = (-1)*n
    z = fibonaci(n)
    if n%2 == 0:
        print(-1)
        print(z%1000000000)
    else:
        print(1)
        print(z%1000000000)
else:
    print(1)
    print(fibonaci(n)%1000000000)
