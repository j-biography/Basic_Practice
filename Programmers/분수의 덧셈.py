
# Q :
# 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 
# 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 
# 두 분수를 더한 값을 '기약 분수'로 나타냈을 때 
# 분자와 분모를 순서대로 담은 배열을 return 하도록 
# solution 함수를 완성해보세요.

# Constraints :
# 0 <numer1, denom1, numer2, denom2 < 1,000

num1, num2, dem1, dem2 = map(int, input().split())

dem3 = max(dem1, dem2)

