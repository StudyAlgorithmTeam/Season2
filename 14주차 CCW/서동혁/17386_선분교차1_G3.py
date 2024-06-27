P1_x1,P1_y1,P1_x2,P1_y2 = map(int,input().split()) # p1, p2
P2_x1,P2_y1,P2_x2,P2_y2 = map(int,input().split()) # p3, p4

p1 = P1_x1,P1_y1
p2 = P1_x2,P1_y2
p3 = P2_x1,P2_y1
p4 = P2_x2,P2_y2

def cross(x1,y1,x2,y2,x3,y3):
    return x1*y2 + x2*y3 + x3*y1 - (y1*x2 + y2*x3 + y3*x1)

#if outer1 * outer2 == 0:
#    print(0)
if (cross(*p1, *p2, *p3) * cross(*p1, *p2, *p4)) < 0 and (cross(*p3, *p4, *p1) * cross(*p3, *p4, *p2)) < 0:
    print(1)
else:
    print(0)

