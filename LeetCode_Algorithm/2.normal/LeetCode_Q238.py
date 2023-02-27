
# Q238. 
# Input 배열을 입력받아 Output 배열을 리턴하라.
# 단 Output[i]에는 Input[i]을 제외한 나머지 Input 요소들의 곱 결과가 들어가야 한다.
# 모든 요소를 곱해놓고 Input[i]를 나누는 방식을 사용해서는 안된다.

# 브루트 포스 방식으로 다 곱하기.
# 재활용 과정이 전혀 없다보니, Timeout 발생

nums = [-1,1,0,-3,3]
output = []

for i in range(len(nums)):
    total = 1
    for j in range(1, len(nums)):
        total *= nums[i-j]
    output.append(total)
    
print(output)
    

