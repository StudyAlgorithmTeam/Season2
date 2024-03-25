import sys
input = sys.stdin.readline

def fibonaci(i):
    farr = [0, 1]
    for j in range(2, i + 1): 
        farr.append(farr[j - 1] + farr[j - 2])  
    return farr[i]

n = int(input())

if n == 0:
    print(0)
    print(0)
elif n == 1:
    print(0)
    print(1)
elif n < 0:
    n = (-1) * n
    z = fibonaci(n)
    if n % 2 == 0:
        print(-1)
        print(z % 1000000000)
    else:
        print(1)
        print(z % 1000000000)
else:
    print(1)
    print(fibonaci(n) % 1000000000)
