
# Q.78
# 모든 부분 집합을 리턴하라

# 기존 방식과 세밀한 검증을 위한 조건(sorted(l)) 추가하여 코딩
# 실패(Timeout)
'''
nums = [1,2,3,4,5,6,7,0]
result = []
l = []

def total():
    if l not in result and sorted(l) not in result:
        result.append(sorted(l).copy())
    
    for i in nums:
        if i not in l:
            l.append(i)
            total()
            l.pop()
            
    return sorted(result)

print(total())
'''
    
    
# 매번 l not in 여부를 검증하지 않게끔 코딩을 해야 시간초과에서 자유로울 것으로 보임.

nums = [0]
result = []
l = []

def total():
    result.append(l.copy())

    for i in nums:
        if len(l) == 0 or (i not in l and i > l[-1]):
            l.append(i)
            total()
            l.pop()
            
    return result
print(total())
        
