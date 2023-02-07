
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

