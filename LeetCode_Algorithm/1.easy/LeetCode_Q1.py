# Q1. 두 수의 합

# 브루트 포스 방식.
'''
# nums = [2, 7, 11, 15] 
# target = 26

# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print(nums[i],nums[j])
'''           
### 에러 발생
'''
# nums = [3, 3]
# nums_2 = []
# nums_3 = []
# target = 6

# for i in range(len(nums)):
#     if nums[i] <= target:
#         nums_2.append(nums[i])

# for j in range(len(nums_2)):
#     if target - nums_2[j] in nums_2:
#         nums_3.append(nums.index(nums_2[j]))
#         nums_3.append(nums.index(target - nums_2[j]))
#         break
        
# print(nums_3)
'''
### 통과. 그러나 enumerate 리스트로 더 가독성있는 코드 작성 가능.
'''

nums = [3, 3, 0, 0, 3, 0, 5]

target = 6

for i in range(len(nums)):
     first = target - nums[i]
     if first in nums[i+1:]:
         print(nums.index(nums[i]), nums[i+1:].index(first)+(i+1))
         break

'''
### 상기 코드를 enumerate(열거) 자료형으로 재 구성.
'''
nums = [2, 1, 0, 5]

target = 6

for i, num in enumerate(nums):
    first = target - num
    if first in nums[i+1:]:
        print(nums.index(num), nums[i+1:].index(first)+(i+1))
        '''
        
# enumerate() 자료형 사용 + 딕셔너리 추가 생성 + 첫번째로 찾은 수 빼고 계산

nums = [2, 7, 11, 15]
target = 9
nums_reverse = {}

for k, v in enumerate(nums):
    nums_reverse[v] = k
    
for k, v in enumerate(nums):
    first = target - v
    if first in nums_reverse and k != nums_reverse[first]:
        print(k, nums_reverse[first])
        break


# 람다 표현식을 기본형으로 사용하는 예제
'''
A = list(map(lambda x : x*2, range(10)))
print(A)
'''
# 람다 표현식을 key 값으로 사용하는 예제
'''
A = ['abc','ee','i']
A.sort(key = lambda x : len(x))
print(A)
'''