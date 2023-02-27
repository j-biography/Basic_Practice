
# Q15. 배열 nums를 입력받아 합으로 0을 만들 수 있는 요소 3개를 출력하라.

# itertools 라이브러리를 사용하는 방법.
# 타임아웃 뜨도록 문제 설계해둠.
# 어찌됐건 하기의 코드에서 배운 것, 
# 리스트 자료형은 set으로 중복 제거가 불가하지만, 튜플 자료형으로 바꾸면 제거 가능.

from itertools import combinations

nums = [-1,0,1,2,-1,-4] 
l = list(combinations(nums, 3))
l2 = []

for i in range(len(l)):
    if sum(l[i]) == 0:
        l2.append(tuple(sorted(l[i])))

l3 = list(set(l2))
l4 = []

for j in range(len(l3)):
    l4.append(list(l3[j]))
    
print(l4)
    
# 브루트 포스로 계산

nums = [-1, 0, 1, 2, -1, -4]
nums.sort() # 정렬 후에는 [-4, -1, -1, 0, 1, 2]
result = []

for i in range(len(nums)-2): # 인덱스 0에서 3까지만 탐색하도록
    if i > 0 and nums[i] == nums[i-1]: # 전자는 인덱스 오류 방지를 위함이며, 후자는 한번 쓴 요소를 다시 쓰지 않기 위한 조건.
        continue
    
    for j in range(i+1, len(nums)-1): # i가 사용한 요소 다음 자리부터 탐색
        if j > i+1 and nums[j] == nums[j-1]: # j 인덱스가 i+1을 넘어간 후에 후자 조건이 성립해야만 continue
            continue
        
        for k in range(j+1, len(nums)):
            if k > j+1 and nums[k] == nums[k-1]:
                continue
            
            if nums[i] + nums[j] + nums[k] == 0:
                result.append([nums[i], nums[j], nums[k]])
                
print(result)
            
# 투 포인터로 좁혀 나가며(narrow down) 계산 

nums = [-1, 0, 2, 4, -1, 7, -3, -4, -5, 0, 2, 1]
nums.sort()
result = []

for i in range(len(nums)-2):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    
    left, right = i+1, len(nums)-1 # 범위는 'i+1'에서 '배열 맨 끝' 사이를 좁혀 들어감.
    while left < right:
        sum = nums[i] + nums[left] + nums[right]
        if sum < 0: # 합이 0보다 작다면 left를 오른쪽으로 옮겨준다.(더 큰 숫자 필요)
            left += 1
        elif sum > 0: # 합이 0보다 크다면 right를 왼쪽으로 옮겨준다.(더 작은 숫자 필요) 
            right -= 1
        else: # 합이 0이라면
            result.append([nums[i], nums[left], nums[right]])
            
            while left < right and nums[left] == nums[left+1]:
                left += 1 # 중복값이 있으면 무시하면서 진행
            while left < right and nums[right] == nums[right-1]:
                right -= 1 # 중복값이 있으면 무시하면서 진행
            left += 1 # 남은 범위 내에서 0을 만들 조합이 더 남아있는지 탐색하면서
            right -= 1 # left > right가 될 때까지 계속 진행
            
print(result)
            
        


        