
# Chapter_04(구현) - Q1(상하좌우)

# 자체 코딩.ver1
'''
n = int(input())

move = input().split()

x = 1
y = 1

for way in move:
    if way == 'L' and y != 1:
        y -= 1
    elif way == 'R' and y != n:
        y += 1
    elif way == 'U' and x != 1:
        x -= 1
    elif way == 'D' and x != n:
        x += 1
    else:
        continue
    
print(x, y)
'''

# 책.ver1
'''
n = int(input())

plans = input().split() # str 타입인 경우 바로 이렇게 받아도 무방

x,y = 1,1

dx = [0,0,-1,1] # L,R,U,D에 따른 X좌표 변경사항
dy = [-1,1,0,0] # L,R,U,D에 따른 Y좌표 변경사항
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)
'''
    
# Chapter_04(구현) - Q2(시각)

# 자체 코딩.ver == 책.ver
'''
N = int(input())
count = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            num = list(str(i)+str(j)+str(k))
            if '3' in num:
                count += 1
                
print(count)
'''

# Chapter_04(구현) - Q3(왕실의 나이트)

# 자체 코딩.ver1
'''
alpha = ['a','b','c','d','e','f','g','h']
pos = list(input()) # 자동으로 X좌표 값과 Y좌표 값이 나뉘어 저장되도록
pos[0] = alpha.index(pos[0])+1 # 미리 정리해둔 alpha 리스트에서 인덱스를 찾아 숫자로 변환
step = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
count = 0

for i in range(8):
    if 0 < int(pos[0]) + step[i][0] <= 8 \
        and 0 < int(pos[1]) + step[i][1] <= 8:
            count += 1

print(count)
'''

# 책.ver1
'''
input_data = input()

column = int(ord(input_data[0])) - int(ord('a')) + 1 
# 알파벳으로 표기되어 있는 column 값을 숫자 형태로 변환하기 위해 ord() 메서드를 사용한다. 
# 알파벳 'A'를 아스키 코드로 변환시 65가 산출되므로, 이를 1로 변환해주기 위한 일련의 과정을 거친다.
row = int(input_data[1])

steps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
# 차후 수정을 요하지 않는 고정된 데이터 값에 대해서는 튜플로 저장을 하는 것이 좋다.
# 튜플은 전체적인 용량, 퍼포먼스 능력이 리스트에 비해 우월하다.

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    
    if next_row >= 1 and next_row <= 8 and \
        next_column >= 1 and next_column <= 8:
            result += 1
            
print(result)
'''

# Chapter_04(구현) - Q4(게임 개발)

# 자체 코딩.ver1

N, M = map(int, input().split())

