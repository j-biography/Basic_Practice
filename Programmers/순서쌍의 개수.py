
# Question: 순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로,(a, b)로 표기합니다. 
# 자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 
# return하도록 solution 함수를 완성해주세요.
# Solution : 약수의 개수를 구한다.


# 정규 수학 학습 과정에서 배운, 인수분해 후 인수의 차수(+1)끼리 곱하는 방식을 구현

def solution(n):
    num = []

    while n != 1:
        for i in range(2, n+1):
            if n % i == 0:
                num.append(i)
                n //= i
                break # for 문을 탈출하여 다시 2부터 나누도록
                
    num2 = set(num)
    result = 1

    for i in num2:
        result *= num.count(i)+1

    return result

# 처음부터 약수를 하나씩 구하고 마지막에 개수를 세는 방식.

n = 100
num = []

for i in range(1,n+1):
    if n % i == 0:
        num.append(i)
        
print(num)