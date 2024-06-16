# 선분 교차 1


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

p1 = x1, y1
p2 = x2, y2
p3 = x3, y3
p4 = x4, y4


def ccw(x1, y1, x2, y2, x3, y3):
    return (x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3)


if (ccw(*p1, *p2, *p3) * ccw(*p1, *p2, *p4)) <= 0 and (ccw(*p3, *p4, *p1) * ccw(*p3, *p4, *p2) <= 0):
    print(1)
else:
    print(0)
