# 백준 1003 # 
# 피보나치 수열 #


# def fibo(N):
#     a, b = 0, 1
#     if N == 0:
#         a, b = 0, 0
#     for i in range(N-1):
#         a, b = b, a+b
    
#     return a, b

# d = fibo(10)
# print(d)



T = int(input())

def fibonacci(N):
    a, b = 0, 1
    if N == 0:
        a, b = 1, 0
    elif N == 1:
        a, b = 0, 1
    else:
        for i in range(N-1):
            a, b = b, a+b
    print(a, b)

for i in range(T):
    fibonacci(int(input()))
