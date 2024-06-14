# 선분 교차 2


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

p1 = x1, y1
p2 = x2, y2
p3 = x3, y3
p4 = x4, y4



def ccw(x1, y1, x2, y2, x3, y3):
    return (x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3)


def range_check():
    return not bool(
        max(x1, x2) < min(x3, x4) or
        max(x3, x4) < min(x1, x2) or
        max(y1, y2) < min(y3, y4) or
        max(y3, y4) < min(y1, y2)
    )


def intersects() -> bool:
    return bool(
        (ccw(*p1, *p2, *p3) * ccw(*p1, *p2, *p4) <= 0) and
        (ccw(*p3, *p4, *p1) * ccw(*p3, *p4, *p2) <= 0) and
        range_check()
    )


if intersects():
    print(1)
else:
    print(0)
