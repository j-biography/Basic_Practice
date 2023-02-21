
# 10872

# 팩토리얼 값을 for 문으로 구하기
# 정수 N이 주어질 때, N!값을 출력
'''
N = 10
sum = 1

for i in range(N, 0, -1):
    sum *= i
print(sum)
'''

# 팩토리얼 값을 재귀 함수로 구하기
'''
N = int(input())

def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)

print(factorial(N))
'''

# 10870

# 피보나치 수를 for 문으로 구하기
'''
N = int(input())

a, b = 0, 1

if N <= 1:
    print(N)
else:
    for i in range(1, N):
        a, b = b, a+b
    print(b)
'''

# 피보나치 수를 재귀 함수로 구하기
'''
N = 10
sum = 0

def fibo(x):
    global sum
    sum += 1
    if x <= 1:
        return x
    else:
        return fibo(x-1) + fibo(x-2)
    
print(fibo(N))
print(sum)
'''

# 피보나치 수를 DP - 하향식 - 메모이제이션으로 구하기

dict = {}

def fibo(n):
    if n in dict:
        return dict[n]
    else:
        if n <= 1:
            return n
        dict[n] = fibo(n-2) + fibo(n-1)
        return dict[n]
    
print(fibo(10))

# 피보나치 수를 DP - 상향식 - 타뷸레이션으로 구하기

dict = {}

def fibo(n):
    for i in range(n+1):
        if i <= 1:
            dict[i] = i
        else:
            dict[i] = dict[i-2] + dict[i-1]
    return dict[n]
    
print(fibo(10))
