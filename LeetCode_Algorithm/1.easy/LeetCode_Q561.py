
# Q561. n개의 페어를 이용한 min(페어1) + min(페어2)의 합으로 만들 수 있는 가장 큰 수를 출력하라.

# 1. 간단한 오름차순 풀이

nums = [1,4,3,2]
nums.sort()

l = [[nums[2*i], nums[(2*i)+1]] for i in range(int(len(nums)/2))]
sum = 0
for i in range(len(l)):
    sum += l[i][0]
    
print(sum)


# 2. 간단한 오름차순 풀이2 (책.Ver)

nums = [1,4,3,2]
sum = 0
pair = []
nums.sort()

for n in nums:
    pair.append(n) # pair 리스트를 채움
    if len(pair) == 2: # pair 리스트에 2개의 요소가 차면,
        sum += min(pair) # pair의 최솟값을 추출해주고,
        pair = [] # pair 리스트는 다시 초기화
        
print(sum)


# 3. 짝수 index에 위치한 수 모두 더하기.
# 발상의 전환. 굳이 어렵게 생각하지 않아도 창의력있게 해결할 수 있음을 보여주는 예

nums = [1,4,3,2]
nums.sort()
sum = 0

for i in range(len(nums)):
    if i % 2 == 0:
        sum += nums[i]
        
print(sum)


# 4. 파이썬답게 매우 간단히(Pythonic Way)

nums = [1,4,3,2]
print(sum(sorted(nums)[::2])) # 가급적 sum을 변수명으로 사용하지 말자. 변수명으로 쓸거면 total을 사용하자.
