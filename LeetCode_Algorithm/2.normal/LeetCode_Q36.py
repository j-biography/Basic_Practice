
# Q.36
# 숫자로 이루어진 배열 candidates를 조합하여 합이 target이 되는 요소를 나열하라.
# 배열에는 같은 숫자가 들어있지 않고, 요소는 여러번 사용이 가능하다.

nums = [2,3,5]
result = []
combi = []
target = 8

def total():
    if sum(combi) == target:
        result.append(combi.copy())
        return
    elif sum(combi) > target:
        return
    for i in nums:
        if len(combi) == 0 or i >= combi[-1]:
            combi.append(i)
            total()
            combi.pop()
        
total()
print(result)
        