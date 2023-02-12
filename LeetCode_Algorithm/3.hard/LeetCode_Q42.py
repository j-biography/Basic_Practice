# Q42. 빗물 트래핑

# 1번 해설 - 투 포인트
'''
height = [0,1,0,2,1,0,1,3,3,1,2,1]

volume = 0

left, right = 0, len(height)-1

left_height, right_height = height[left], height[right]

while left < right:
    left_height = max(height[left], left_height)
    right_height = max(height[right], right_height)
    
    if left_height <= right_height:
        volume += left_height - height[left]
        left += 1
    
    else:
        volume += right_height - height[right]
        right -= 1
    
print(volume)
'''

# 2번 해설 - 스택

height = [0,1,0,2,1,0,1,3,2,1,2,1]

stack = []

volume = 0

for i in range(len(height)):
    # while bool(stack) == True and height[i] > height[stack[-1]]:
    while stack and height[i] > height[stack[-1]]:
        max = stack.pop()
        
        # if bool(stack) == False:
        if not stack:
            break
        
        distance = i - stack[-1] -1
        water = min(height[i], height[stack[-1]]) - height[max]
        volume += (distance * water)
        
    stack.append(i)
print(volume)


