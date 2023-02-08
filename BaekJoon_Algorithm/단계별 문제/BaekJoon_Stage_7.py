
# 1712

# 판매량 변수를 하나씩 늘려나가면서, 
# (노트북가격 * 판매량)값이 (고정비용+(가변비용*판매량))값을 초과하는 D 지점을 찾으려하면 시간이 초과할 수 있음.
'''
A, B, C = map(int, input().split())

D = 0

if B >= C:
    print('-1')
else:
    while True:
        if A+(B*D) >= (C*D):
            D += 1
        else:
            print(D)
            break
            '''
            
'''  
A, B, C = map(int, input().split())

if B >= C:
    print('-1')
else:
    print(A//(C-B)+1)
    '''
    
# 2292

'''
N = int(input())
way = 1
crust = 1

while True:
    if crust < N and N != 1:
        crust += (6*way)
        way += 1
    elif N == 1:
        break
    else:
        break
    
print(way)'''

'''
N = int(input())

count = 1
way = 1

while count < N:
    count += way * 6
    way += 1
else:
    print(way)
    '''
    
    
# 1193

# X = int(input())

# num = 1
# count = 1
# rest = 0

# while X > num:
#     rest = X%num
#     num += count+1
#     count += 1

# sum = count+1

# a = list(range(1,sum))

# if sum%2 == 0:
#     print(f'{a[-rest]}/{a[rest-1]}')
# else:   
#     print(f'{a[rest-1]}/{a[-rest]}')

# print(a)

# N = int(input())

# num = 3
# line = 3
# rest = 1

# if N <= 1:
#     line -= 2
# elif N <= 3:
#     line -= 1
#     rest = N%2
# while num < N:
#     rest = N % num
#     num += line + 1
#     line += 1
# else:
#     list = []
#     for i in range(1,line):
#         list.append(i)

# print(rest)
# print(list)



# 변수 이름을 잘 설정하자.
# 내가 생성한 변수의 역할을 내가 잊음.

'''
x = int(input())

line = 1
lineValue = 1

while lineValue < x:
    line += 1
    lineValue += line
else:
    rest = line-(lineValue-x)

if line % 2 == 0:
    print(f'{rest}/{line-(rest-1)}')
else:
    print(f'{line-(rest-1)}/{rest}')
    '''
    
# 2869

# 시간초과 버전
'''
A, B, V = map(int, input().split())

high = 0
day = 0

while high < V:
    high += A
    if high < V:
        high -= B
        day += 1
    else:
        day += 1
else:
    print(day)
'''

'''
A, B, V = map(int, input().split())

value = (V/(A-B)) - (B/(A-B))

if value == int(value):
    print(int(value))
else:
    print(int(value+1))
    '''
    
# 10250

'''
T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    
    floor = N%H
    if floor == 0:
        floor = H
    room = N//H
    if N/H != N//H:
        room = (N//H) + 1
    
    if room < 10:
        print(f'{floor}0{room}')
    elif room >= 10:
        print(f'{floor}{room}')     
        '''
        
        
# 2775

# 아파트 호수별로 리스트를 구현한 다음, 해당 호수의 값 리턴
'''
T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    num = []
    for room in range(1, n+1):
        num.append(room)
    for floor in range(k):
        for room in range(1, n):
            num[0] = 1
            num[room] = num[room-1] + num[room]
                
    print(num[-1])
    '''

# 재귀 함수 방식으로, 값 리턴 - 시간 초과
'''
def apt(k, n):
    sum = 0
    if k == 1:
        for room in range(1, n+1):
            sum += room
    else:
        for room in range(1, n+1):
            sum += apt(k-1, room)
    return sum

   
T = int(input())

for test in range(T):      
    k = int(input())
    n = int(input())
    print(apt(k, n))
    '''

# 2839

# (-1) 출력 조건을 미리 넣어준 코드
'''
N = int(input())

if N == 4 or N == 7:
    print(-1)
else:
    share = N // 5
    rest = N % 5
    while rest%3 != 0:
        share -= 1
        rest = N - (share*5)
    else:
        print(share + rest//3)
        '''

# 오히려 이게 미리 (-1) 출력 조건을 넣어준 경우보다 런타임이 짧네..
'''
N = int(input())

share = N // 5
rest = N % 5

while rest % 3 != 0 and share >0 and rest > 0:
    share -= 1
    rest = N - (share*5)
if rest % 3 == 0:    
    print(share + rest//3)
else:
    print(-1)
    '''

# 10757

import sys

A, B = map(int, sys.stdin.readline().split())

print(A+B)