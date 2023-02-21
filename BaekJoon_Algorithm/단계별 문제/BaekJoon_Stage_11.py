
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
N = 10
fibo = [0]

for i in range(N):
    if i == 0:
        fibo.append(1)
    else:
        fibo.append(fibo[i] + fibo[i-1])
    
print(fibo[-1])
'''

# 피보나치 수를 재귀 함수로 구하기

N = 10

def fibo(x):
    if x <= 1:
        return x
    else:
        return fibo(x-1) + fibo(x-2)
    
print(fibo(N))