# 분산처리

# T = int(input())

# def q_1009(a, b):
#     a, b = 0, 0
#     for i in range(T):
#         a, b = map(int, input().split())
#         c = str(a**b)
#         print(c[-1])
    
# q_1009(0, 0)

# a = 10
# b = 145
# c = str(a*b)
# d = int(c[-1])
# print(d)


'''


T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    c = str(a**b)
    print(c[-1])
    
    --- 시간초과 버전 ---
    
    
'''

    
# T = int(input())

# for i in range(T):
#     a, b = map(int, input().split())
#     check = str(a)[-1]
#     if check in ['1','5','6']:
#         print(check)
#     elif check == '0':
#         print('10')
#     elif check in ['4','9'] and b % 2 == 1:
#         print(check)
#     elif check in ['4','9'] and b % 2 == 0:
#         print(str(a**2)[-1])
#     elif check in ['2','3','7','8'] and b < 5:
#         print(str(a**b)[-1])
#     elif check in ['2','3','7','8'] and b >= 5:
#         print(str(a**(b % 4))[-1]) 
        
        
'''
1차 버전, 경우의 수를 모두 if 문에 삽입

T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    
    check = str(a)[-1]
    
    if check in ['0']:
        print(10)
    elif check in ['1','5','6']:
        print(int(check))
    elif check in ['4','9'] and b % 2 == 1:
        print(int(check))
    elif check in ['4','9'] and b % 2 == 0:
        check = str(a**2)[-1]
        print(int(check))
    elif check in ['2','3','7','8'] and b <= 4:
        check = str(a**b)[-1]
        print(int(check))
    elif check in ['2','3','7','8'] and b % 4 != 0:
        check = str(a**(b%4))[-1]
        print(int(check))
    elif check in ['2','3','7','8'] and b % 4 == 0:
        check = str(a**4)[-1]
        print(int(check))
        
        
'''
        

# Final 축약 버전 #
        
T = int(input())

for i in range(T):
    a,b = map(int, input().split())
    
    
    if str(a)[-1] == '0':
        print(10)
    
    elif b < 4:
        print(str(a**b)[-1])
    
    elif b > 4 and b % 4 != 0:
        print(str(a**(b % 4))[-1])
        
    elif b % 4 == 0:
        print(str(a**4)[-1])
    