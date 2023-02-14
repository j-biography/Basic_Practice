
# Q :
# 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 
# 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 
# 두 분수를 더한 값을 '기약 분수'로 나타냈을 때 
# 분자와 분모를 순서대로 담은 배열을 return 하도록 
# solution 함수를 완성해보세요.

# Constraints :
# 0 <numer1, denom1, numer2, denom2 < 1,000


# 정답률 93.3%
'''
num1, num2, dem1, dem2 = map(int, input().split())

dem3 = max(dem1, dem2)

while dem3 % dem1 != 0 or dem3 % dem2 != 0:
    dem3 += 1
    
num1 = num1 * (dem3/dem1)
num2 = num2 * (dem3/dem2)
num3 = num1 + num2

for i in range(2, dem3+1):
    if num3 % i == 0 and dem3 % i == 0:
        num3 = num3 / i
        dem3 = dem3 / i
        
print([num3, dem3])
'''

# 정답률 100%
'''
def solution(numer1, denom1, numer2, denom2):
    
    denom3 = denom1 * denom2
    
    numer3 = numer1 * (denom3/denom1) + numer2 * (denom3/denom2)
    
    for i in range(denom3, 1, -1):
        if denom3 % i == 0 and numer3 % i == 0:
            denom3 /= i
            numer3 /= i
            
    return [numer3, denom3]
    '''

