def is_prdrop(N):
    if str(N) == str(N)[::-1]:
        return N
    else:
        return False

def prdrop(N):
    while True:
        N += 1
        if is_prdrop(N):
            return N

N = int(input())
r = prdrop(N)
print(r)
        
