
# 2739

'''

N = int(input())

for i in range(1,10):
    print(N,'*',i,'=',N*i)
    
'''

# 10950

'''

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    
    print(A+B)
    
'''
    
# 8393 - original

'''

n = int(input())
a = []

for i in range(n+1):
    a.append(i)
    a2 = sum(a)
    
print(a2)

'''

# 8393 - short

'''

n = int(input())

print((n*(n+1))//2)

'''

# 25304

'''

X = int(input())
N = int(input())
list = []

for i in range(N):
    a, b = map(int, input().split())
    list.append(a*b)
    list2 = sum(list)
    
if X == list2:
    print('Yes')
else:
    print('No')
    
'''

# 15552

'''

import sys

T = int(sys.stdin.readline())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)
    

import sys

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(A+B)
    
    
import sys

T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)
    
'''

# 11021, 11022

'''

import sys

T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    
    a = f'Case #{i}: {A+B}'
    print(a)
    

import sys

T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    
    print(f'Case #{i+1}: {A+B}')
    

import sys

T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    
    print(f'Case #{i+1}: {A} + {B} = {A+B}')
    
'''


# 2438, 2439

'''

T = int(input())

for i in range(T):
    print('*'*(i+1))
    
    
T = int(input())

for i in range(T):
    print(' '*(T-(i+2)),'*'*(i+1))
    

    
T = int(input())

for i in range(T):
    
    space = (' '*(T-(i+1)))
    star = ('*'*(i+1))
    
    print(f'{space}{star}')
    
    '''
    
# 10952

'''

A, B = 1, 1

while A != 0 and B != 0:
    A, B = map(int, input().split())
    print(A+B)
    continue


A, B = map(int, input().split())

while A != 0 and B != 0:
    print(A+B)
    A,B = map(int, input().split())

'''

# 10951

'''
import sys

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    
    except EOFError:
        break
'''

### 입력이 끝나면 종료하는 기능 구현.
### EOFError 기능을 사용하기.
### End of File



# 1110


# N = input()
# count = 0

# while True:
#     try:
#         if int(N) < 10:
#             a = N+'0'
#             count += 1
            
#             b = a[1]
#             c = int(a[0])+int(a[1])
#             a = b+str(c)
        
             
#         else:
#             a = N
        
#             b = a[1]
#             c = int(a[0])+int(a[1])
        
#             a = b+str(c)
        
#             count += 1
        
#     except count == int(N):
#         break

# print(count)

'''

N = input()
count = 0

while True:
    if int(N) < 10:
        a = '0'+N
        break
        
    else:
        a = N
        break
        
while True:    
    b = a[1]
    c = int(a[0]) + int(a[1])
    d = str(c)
    a = b+d[-1]
    count += 1
    
    if a == N or a == '0'+N:
        break
    
print(count)

'''

