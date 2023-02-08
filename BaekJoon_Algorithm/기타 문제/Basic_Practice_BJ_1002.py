import math

T = int(input())

for i in range(T):
    a = list(map(int, input().split()))

    x1 = a[0] 
    y1 = a[1] 
    r1 = a[2] 

    x2 = a[3] 
    y2 = a[4] 
    r2 = a[5] 

    D = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

    if D > abs(r2 - r1) and D < r1 + r2:
        print('2')
    elif D == r1 + r2:
        print('1')
    elif D != 0 and D == abs(r2 - r1):
        print('1')
    elif D > r1 + r2:
        print('0')
    elif D < abs(r2 - r1):
        print('0')
    elif D == 0 and r1 == r2:
        print('-1')