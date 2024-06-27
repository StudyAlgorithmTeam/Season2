import sys

sys.stdin = open('c:/Users/서동혁/OneDrive/바탕 화면/BAEKJOON/.vscode/stdin.txt', 'r')
print()

P1_x1,P1_y1,P1_x2,P1_y2 = map(int,input().split()) # p1, p2
P2_x1,P2_y1,P2_x2,P2_y2 = map(int,input().split()) # p3, p4

p1 = P1_x1,P1_y1
p2 = P1_x2,P1_y2
p3 = P2_x1,P2_y1
p4 = P2_x2,P2_y2

def cross(x1,y1,x2,y2,x3,y3):
    return x1*y2 + x2*y3 + x3*y1 - (y1*x2 + y2*x3 + y3*x1)

def check(x1,y1,x2,y2,x3,y3,x4,y4) -> bool:
    """두 선분이 동일선상에 있을 때 안겹치는지 여부"""
    return max(x1,x2) < min(x3,x4) or max(y1,y2) < min(y3,y4)

#if outer1 * outer2 == 0:
#    print(0)
if (cross(*p1, *p2, *p3) * cross(*p1, *p2, *p4)) == 0 and (cross(*p3, *p4, *p1) * cross(*p3, *p4, *p2)) == 0:
    if check(*p1, *p2, *p3, *p4) or check(*p3, *p4, *p1, *p2):
        print(0)
    else:
        print(1)
elif (cross(*p1, *p2, *p3) * cross(*p1, *p2, *p4)) <= 0 and (cross(*p3, *p4, *p1) * cross(*p3, *p4, *p2)) <= 0:
    print(1)
else:
    print(0)