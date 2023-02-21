
# 15596

'''

a = [1,2,3,4,5,6,7,8,9]

def solve(a):
    ans = 0
    
    for i in range(len(a)):
        if len(a[i]) > 1:
            for j in range(len(a[i])):
                ans += a[i][j]
                if len(a[i][j]) == 1:
                    continue
                else:
                    print('break')
        else: 
            ans += a[i]
    
    print(ans)
    return ans
    
solve(a)

'''

# a = [1,2,3,4,5]

# for i in range(a):
#     b = sum(a[0:])

# print(b)

# sum() 메서드를 사용하여 구현

'''
# a = [1,2,3]

# def plus(a):
#     ans = 0
#     ans = sum(a)
#     return ans

# print(plus(a))
'''

# 합을 구하는 코드를 작성하여 구현

'''
a = [1,2,3,4,5]

def plus(a):
    ans = 0
    for i in range(len(a)):
        ans += a[i]
    return ans

print(plus(a))
'''

# 4673

'''
a = list(range(10000))

for n in range(10000):
    if n < 10:
        x = (n + n)
        if x in a:
            a.remove(x)
        else:
            continue
    if 10 <= n < 100:
        x = n + int(str(n)[0]) + int(str(n)[1])
        if x in a:
            a.remove(x)
        else:
            continue
    if 100 <= n < 1000:
        x = n + int(str(n)[0]) + int(str(n)[1]) + int(str(n)[2])
        if x in a:
            a.remove(x)
        else:
            continue
    if 1000 <= n < 10000:
        x = n + int(str(n)[0]) + int(str(n)[1]) + int(str(n)[2]) + int(str(n)[3])
        if x in a:
            a.remove(x)
        else:
            continue
        
        
for i in range(len(a)):
    print(a[i])
    '''
    
# 상기 코드를 축약하여 재코딩

'''
# 브루트포스 + 소거법으로 풀이 #

a = list(range(10000+1)) # 문제 조건에 따라 10000보다 작거나 같은 자연수를 포함한 리스트 생성.

for n in range(10000+1):
    x = n
    for i in range(len(str(n))): # 정수 n의 총 글자수 인식. 
        x += int(str(n)[i]) 
        
    if x in a:
        a.remove(x) 
        # x 값이 a 내에 없을 경우 ValueError가 발생하기에, x값이 a 내에 있는지 확인 후 remove()로 삭제.
        
    else:
        continue

for j in range(len(a)): # 리스트 형태를 풀어서 출력하기 위한 코드.
    print(a[j])
    '''

# try - except 구문으로 ValueError 예외처리

'''
a = list(range(10000+1)) # 문제 조건에 따라 10000보다 작거나 같은 자연수를 포함한 리스트 생성.

for n in range(10000+1):
    x = n
    for i in range(len(str(n))): # 정수 n의 총 글자수 인식. 
        x += int(str(n)[i]) 
        
    try:
        a.remove(x) 
        
    except ValueError:
        continue
    # ValueError의 예외처리는 try - except 구문으로.
    
for j in range(len(a)): # 리스트 형태를 풀어서 출력하기 위한 코드.
    print(a[j])
    '''

# 1065

'''
sequence = []

N = int(input())

for x in range(1, 1000+1):
    if 1 <= x < 100 and x <= N: # 100보다 작은 자연수는 모두 한수, 그 중 N보다 작은 한수만 추출하여 append
        sequence.append(x)
    
    elif 100 <= x < 1000 and x <= N:
        if int(str(x)[2]) - int(str(x)[1]) == int(str(x)[1]) - int(str(x)[0]):
            sequence.append(x)
    
    else:
        continue
    
print(len(sequence)) # 조건을 충족하는 한수의 개수 출력
'''
'''
sequence = []

N = int(input())

for x in range(1, 1000+1):
    count = 0
    for i in range(len(str(x))):
        count += int(str(x)[i])
    if count == 

print(sequence)
'''
# 하나의 조건문으로 압축시키는 코드 작성 - 아직 미해결

            

