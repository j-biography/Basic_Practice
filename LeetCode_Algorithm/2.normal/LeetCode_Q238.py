
# Q238. 
# Input 배열을 입력받아 Output 배열을 리턴하라.
# 단 Output[i]에는 Input[i]을 제외한 나머지 Input 요소들의 곱 결과가 들어가야 한다.
# 모든 요소를 곱해놓고 Input[i]를 나누는 방식을 사용해서는 안된다.

# 브루트 포스 방식으로 다 곱하기.
# 재활용 과정이 전혀 없다보니, Timeout 발생
'''
nums = [-1, 1, 0, -3, 3]
output = []

for i in range(len(nums)):
    total = 1
    for j in range(1, len(nums)):
        total *= nums[i-j]
    output.append(total)
    
print(output)
    '''

# 재활용 방식으로 곱하기.
# i의 왼쪽에서 곱해나가는 값은 저장하고, 이를 재활용
# i의 오른쪽에서 곱하는 행위만 계속 반복
# 타임아웃
'''
nums = [1,2,3,4]
output = []
left = 1

for i in range(len(nums)):
    if i == 0:
        left *= 1
    else:
        left *= nums[i-1] # i 왼쪽 값을 계속 곱하면서 나아감
    right = 1
    for j in range(len(nums)-1, i, -1):
        right *= nums[j]
        
    output.append(left * right)
    
print(output)
'''


# 재활용 방식으로 곱하기. (왼쪽, 오른쪽 모두 재활용)
# 왼쪽에서 곱해나가는 값을 미리 output 배열에 왼쪽부터 저장해두고,
# 나중에 오른쪽에서 곱해나가는 값을 output 배열 맨 오른쪽 요소부터 곱해나감.
# 성공

nums = [1,2,3,4]
output = []
left = 1
right = 1

for i in range(len(nums)):
    output.append(left)
    left *= nums[i] 
    
for j in range(len(nums)-1, -1, -1):
    output[j] = output[j] * right
    right *= nums[j] 
    
print(output)
    

    





