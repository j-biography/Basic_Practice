
# Q.121
# 배열을 입력 받아 한번의 거래로 낼 수 있는 최대 이익을 산출하라.
# 단 최대 이익 arr[i] - arr[j]을 산출했을 경우 반드시 i > j 이어야 한다.
# 산출되는 이익이 없을 경우 0을 리턴하라.

# 1. 왼쪽부터 최솟값, 최댓값, 차이값을 갱신하면서 진행(성공)

nums = [7,6,4,3,1]
minimum = nums[0]
maximum = nums[0]
diff = 0

for i in range(len(nums)):
    if nums[i] < minimum:
        minimum = nums[i]
        maximum = nums[i]
    elif nums[i] > maximum:
        maximum = nums[i]
        if maximum - minimum > diff:
            diff = maximum - minimum

print(diff)

# 2. 책 Ver. 방법은 유사하나 더욱 단순하게 코딩(성공)

import sys

prices = [7,6,4,3,1]
diff = 0
minimum = sys.maxsize

for n in prices:
    minimum = min(minimum, n)
    diff = max(diff, n - minimum)
    
print(diff)

# 2-1. 책 Ver의 sys.maxsize를 max() 메서드로 변환하여 테스트(성공)

prices = [7,6,4,3,1]
diff = 0
minimum = max(prices)

for n in prices:
    minimum = min(minimum, n)
    diff = max(diff, n - minimum)
    
print(diff)


