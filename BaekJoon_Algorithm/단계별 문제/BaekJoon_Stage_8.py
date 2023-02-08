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

