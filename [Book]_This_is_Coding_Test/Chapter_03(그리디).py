
# Chapter_03(그리디) - Q2(큰 수의 법칙)

# 자체 코딩.Ver
'''
N, M, K = map(int, input().split())

Arr = list(map(int, input().split()))

Arr.sort()

sum = 0
count = 0

for i in range(M):
    if count == K:
        sum += Arr[-2]
        count = 0
        continue
    
    sum += Arr[-1]
    count += 1
    
print(sum)
'''

# 책.Ver1
'''
N, M, K = map(int, input().split())

Arr = list(map(int, input().split()))

Arr.sort()
first = Arr[N-1]
second = Arr[N-2]

result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        
        result += first
        M -= 1
        
    if M == 0:
        break
    
    result += second
    M -= 1
    
print(result)
'''   

# 자체 코딩.Ver2 
'''
N, M, K = map(int, input().split())

Arr = list(map(int, input().split()))

Arr.sort()

first = Arr[N-1]
second = Arr[N-2]

sum_r = (first*K + second) # 한 번의 루틴 당 수의 합
routine =  M // (K+1) # 총 몇 번의 루틴을 돌아야 하는지 산출
rest =  M % (K+1) # 루틴을 모두 돌고 나머지 값 

total = ((routine * sum_r) + (first * rest))

print(total)
'''

# 책.Ver2
'''
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += count * first
result += (m-count) * second

print(result)
'''

# Chapter_03(그리디) - Q3(숫자 카드)

# 자체 코딩.ver1
'''
N, M = map(int, input().split())
minimum = 0

for i in range(N):
    nums = list(map(int, input().split()))
    if min(nums) > minimum:
        minimum = min(nums)

print(minimum)
'''

# 자체 코딩.ver2
'''
N, M = map(int, input().split())
final = 0

for i in range(N):
    nums = list(map(int, input().split()))
    minimum = nums[0]
    for num in nums:
        if num < minimum:
            minimum = num
    
    if minimum > final:
        final = minimum

print(final)
'''

# 책.ver1
'''
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
    
print(result)
'''

# 책.ver2
'''
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
        
    result = max(result, min_value)
    
print(result)            
'''

# Chapter_03(그리디) - Q4(1이 될 때까지)

# 자체 코딩.ver1
'''
n, k = map(int, input().split())
count = 0

while n != 1:
    if n % k == 0:
        n /= k
        count += 1
    else:
        n -= 1
        count += 1
      
print(count)
'''

# 자체 코딩.ver2
# 만약 n값이 100억 이상이라면, 어떤 방식으로 빠른 PS를 구현할 것인가.
'''
n, k = map(int, input().split())

total_cnt = 0
k_pow = k

while k_pow <= n:
    k_pow *= k
    total_cnt += 1

rest = n - (k_pow / k)

print(int(total_cnt + rest))
'''

# 책.ver1
'''
n, k = map(int, input().split())

result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
        
    n //= k 
    result += 1
    
while n > 1:
    n -= 1
    result += 1
    
print(result)
'''

# 책.ver2 (While True & if Break 문을 통해 반복 구현 방법을 재학습)

n, k = map(int, input().split())

result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    
    if n < k:
        break
    result += 1
    n //= k 
    
result += (n-1)
print(result)