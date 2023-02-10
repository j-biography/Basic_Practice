# 1978
'''
N = int(input())

nums = list(map(int, input().split()))

count = N

for i in range(N):
    for j in range(2, 1000):
        if nums[i] == 1:
            count -= 1
            break
        elif nums[i] != j and nums[i] % j == 0:
            count -= 1
            break
    
print(count)
'''

# 좀 더 간략하게 nums[i] >> for num in nums로 빼버림
'''
N = int(input())
nums = list(map(int, input().split()))
count = N

for num in nums:
    if num == 1:
        count -= 1
    for j in range(2, num+1):
        if num != j and num % j == 0:
            count -= 1
            break
    
print(count)
'''

# 2581

# 시간초과 : 2028ms
'''
M = int(input()) # 첫째 줄에 주어지는 자연수, N보다 작거나 같다.
N = int(input()) # 둘째 줄에 주어지는 자연수
num = list(range(M,N+1))

for i in range(M, N+1):
    for j in range(N+1):
        if i == 1 or j > 1 and i != j and i % j == 0:
            num.remove(i)
            break

if len(num) >= 1:
    print(sum(num))
    print(min(num))
else:
    print('-1')
    '''
    
# 시간초과 : 1056ms
'''
M = int(input())
N = int(input())
prime = []

for i in range(M, N+1):
    for j in range(2, N+1):
        if i == 1 or (i != j and i % j == 0):
            break
        else:
            if i % j != 0:
                continue
            else:
                prime.append(i)
                break
                        
if len(prime) < 1:
    print('-1')
else:
    print(sum(prime))
    print(min(prime))
    '''

# 수의 규칙(제곱근 이하의 수로 나눠지지 않는다면, 그 이상의 수로도 나뉘지 않는다.)
# 116ms
'''
import math

M = int(input())
N = int(input())
prime = []

for i in range(M, N+1):
    for j in range(2, int(math.sqrt(N)+2)):
        if i == 1 or i < j or (i != j and i % j == 0):
            break
        elif i == j or int(math.sqrt(N)+1) == j:
            prime.append(i)
        else:
            continue
           
if len(prime) < 1:
    print('-1')
else:
    print(sum(prime))
    print(min(prime))          
'''

# 소수를 찾아주는 함수를 정의해서 사용
# 52ms
'''
import math

def prime(n):
    for i in range(2, int(math.sqrt(n))+2):
        if n == 1 or n != i and n % i == 0:
            return False
    return True

###############################

M = int(input())
N = int(input())
number = range(M,N+1)
list_prime = []

for j in range(len(number)):
    if prime(number[j]) == True:
        list_prime.append(number[j])


if len(list_prime) < 1:
    print('-1')
else:
    print(sum(list_prime))
    print(min(list_prime))
    '''
    
# 11653  

# 브루트 포스
# 1312ms
'''
N = int(input())

for i in range(2, N+1):
    while N % i == 0:
        N /= i
        print(i)
'''        
        
# 제곱근으로 범위를 축소시켜 브루트 포스
# 44ms
'''
import math

N = int(input())

for i in range(2, int(math.sqrt(N))+2):
    while N % i == 0:
        N /= i
        print(i)
if N > 1:
    print(int(N))
    '''
    
# 1929

# 문제 1978의 52ms 답안 그대로 사용 >>> 4056ms
'''
import math

def prime(n):
    for i in range(2, int(math.sqrt(n))+2):
        if n == 1 or n != i and n % i == 0:
            return False
    return True

M, N = map(int, input().split())

number = range(M,N+1)
list_prime = []

for j in range(len(number)):
    if prime(number[j]) == True:
        print(number[j])
        '''

# 미리 2와 3의 배수 필터링 후 소수 판별 함수에 투입 >>> 3852ms(효과 미미)
'''
import math

def prime(n):
    for i in range(2, int(math.sqrt(n))+2):
        if n == 1 or n != i and n % i == 0:
            return False
    return True

M, N = map(int, input().split())

number = []

for j in range(M, N+1):
    if j > 2 and j % 2 == 0:
        continue
    elif j > 3 and j % 3 == 0:
        continue
    else:
        number.append(j)

for k in range(len(number)):
    if prime(number[k]) == True:
        print(number[k])
'''    
        
# '에라토스테네스의 채' 알고리즘 활용 >>> 600ms
'''
import math

M, N = map(int, input().split())

prime = [True for i in range(N+1)] # 실제 숫자가 아닌 True 값으로만 리스트를 형성하니 시간 소모가 대폭 적어짐.

for i in range(2, int(math.sqrt(N))+1):
    if prime[i] == True:
        j = 2
        while i * j <= N:
            prime[i * j] = False
            j += 1
            
for i in range(M, N+1): # 위에서 한번 쓴 'i'는 다시 써도 됨
    if i != 1 and prime[i] == True:
        print(i)
        '''
        