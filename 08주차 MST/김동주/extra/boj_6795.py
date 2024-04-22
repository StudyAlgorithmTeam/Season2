def calc(fwd, bwd, s):
    dist = (fwd-bwd) * (s//(fwd+bwd)) # dist so far
    rem = s % (fwd+bwd) # dist remains
    if rem <= fwd:
        dist += rem
    else:
        dist += fwd-(rem-fwd)
    return dist


a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

nikky = calc(a, b, s)
byron = calc(c, d, s)

if nikky > byron:
    print('Nikky')
elif nikky < byron:
    print('Byron')
else:
    print('Tied')