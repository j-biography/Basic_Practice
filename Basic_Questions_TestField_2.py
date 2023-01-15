

# print("|\_/|")
# print("|q p|   /}")
# print('( 0 )"""\ ')
# print('|"^"`    |')
# s = '||_/=\ \__|'
# print(s.replace(' ', ''))


# print("         ,r'"+'"7')
# print("r`-_   ,'  ,/")
# print(' \. ".'+" L_r' ")
# print("   `~\/")
# print('      |')
# print('      |')

'''

# A, B = map(int, input().split())

# if A > B:
#     print('>')
# elif A < B:
#     print('<')
# elif A == B:
#     print('==')

# Test = int(input())

# if 100 >= Test >= 90:
#     print('A')
    
# elif 89 >= Test >= 80:
#     print('B')
    
# elif 79 >= Test >= 70:
#     print('C')

# elif 69 >= Test >= 60:
#     print('D')

# else:
#     print('F')


'''

# 윤년 #

'''
Year = int(input())

if Year % 4 == 0:
    if Year % 100 != 0 or Year % 400 == 0:
        print('1')
    else:
        print('0')       
else:
    print('0')
    
'''
 # 사분면 #
 
 
'''

Quadrant 1 : X = plus, Y = plus
Quadrant 2 : X = minus, Y = plus
Quadrant 3 : X = minus, Y = minus
Quadrant 4 : X = plus, Y = minus 


X = int(input())
Y = int(input())

def Quadrant(X, Y):
    if X >= 0 and Y >= 0:
        print(1)
        
    elif X < 0 and Y >= 0:
        print(2)
        
    elif X < 0 and Y < 0:
        print(3)

    elif X >= 0 and Y >= 0:
        print(4)
   
   
   
X = int(input())
Y = int(input())

def Quadrant(X, Y):
    if X >= 0:
        if Y >= 0:
            print(1)
        
        elif Y < 0:
            print(4) 
    
    elif X < 0:
        if Y >= 0:
            print(2)
            
        elif Y < 0:
            print(3)
            
Quadrant(X, Y)

'''

# 2884 알람

'''

X, Y = map(int, input().split())

def Hour(X, Y):
    if 1 <= X <= 23 and Y >= 45:
        X = X
        if 45 <= Y <= 59:
            Y -= 45
        elif Y <= 44:
            Y = Y + 15
            
    elif 1 <= X <= 23 and Y <= 44:
        X -= 1
        if 45 <= Y <= 59:
            Y -= 45
        elif Y <= 44:
            Y = Y + 15
        
    elif X == 0 and Y >= 45:
        X = 0
        if 45 <= Y <= 59:
            Y -= 45
        elif Y <= 44:
            Y = Y + 15  
            
    else:
        X = 23
        if 45 <= Y <= 59:
            Y -= 45
        elif Y <= 44:
            Y = Y + 15  
            
    print(X, Y)
    
Hour(X,Y)

'''

'''
X, Y = map(int, input().split())

def Hour(X, Y):
    if 1 <= X <= 23:
        if 45 <= Y:
            X = X
            Y -= 45
        elif Y <= 44:
            X -= 1
            Y += 15
        
    elif X == 0:
        if 45 <= Y <= 59:
            X = X
            Y -= 45
        elif Y <= 44:
            X = 23
            Y += 15  
            
    print(X, Y)
    
Hour(X,Y)
'''

# 2525 오븐

'''

X, Y = map(int, input().split())
Time = int(input())

def Oven(X, Y):
    
    if Y + Time >= 60:
       
        if (X + (Y + Time) // 60) < 24:
            X += (Y + Time) // 60
            Y = (Y + Time) % 60
        else:
            X = (X + (Y + Time)  // 60) - 24
            Y = (Y + Time) % 60
           
    else:
        X = X
        Y += Time
            
    print(X, Y)
    
Oven(X, Y)

'''

# 2480 주사위

X, Y, Z = map(int, input().split())

def dice(X, Y, Z):
    if X == Y and X == Z:
        print((X * 1000) + 10000)
    
    elif X == Y or X == Z:
        print((X * 100) + 1000)
    
    elif Y == Z:
        print((Y * 100) + 1000)
        
    else:
        if X > Y and X > Z:
            print(X*100)
        elif Y > X and Y > Z:
            print(Y * 100)
        else:
            print(Z * 100)
        
dice(X, Y, Z)

