import math

def solution(nums):
    
    nums.sort()
    max_sum = sum(nums[-1:-4:-1])
    min_sum = sum(nums[0:3])
    
    prime = [i for i in range(min_sum, max_sum+1)]
    
    for i in range(len(prime)):
        for j in range(2, int(math.sqrt(max_sum))+1):
            if prime[i] != j and prime[i] % j == 0 and prime[i] in prime:
                prime.remove(prime[i])
            else:
                continue
    return prime

nums = [1,2,7,6,4]

print(solution(nums))