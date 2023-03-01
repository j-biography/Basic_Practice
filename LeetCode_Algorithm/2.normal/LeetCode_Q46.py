
# Q.46
# 배열을 입력받아 생성 가능한 모든 순열을 출력하라.

nums = [1,2,3,4]
answer = []
l = []

def dfs(nums):
    if len(nums) == 2:
        answer.append(l[:])
        
    for n in nums:
        l.append(n)
        
        new_nums = nums[:]
        new_nums.remove(n)
        dfs(new_nums)
        l.pop()
        
    return answer

print(dfs(nums))



    

        
    
        