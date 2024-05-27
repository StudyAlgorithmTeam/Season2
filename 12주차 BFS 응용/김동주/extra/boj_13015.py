# 별 찍기 - 23

import sys


N = int(sys.stdin.readline())

end = lambda: sys.stdout.write('*'*N + ' '*(2*N-3) + '*'*N + '\n')
bridge = lambda i: sys.stdout.write(' '*i+'*'+' '*(N-2)+'*'+' '*(2*(N-i)-3)+'*'+' '*(N-2)+'*'+'\n')
joint = lambda i: sys.stdout.write(' '*i+'*'+' '*(N-2)+'*'+' '*(N-2)+'*'+'\n')

end()
for i in range(1, N-1):
    bridge(i)
joint(N-1)
for i in reversed(range(1, N-1)):
    bridge(i)
end()
