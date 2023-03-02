
# Q.39
# 숫자로 이루어진 배열 candidates를 조합하여 합이 target이 되는 요소를 나열하라.
# 배열에는 같은 숫자가 들어있지 않고, 요소는 여러번 사용이 가능하다.

nums = [0,2,3,5]
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
        if (i != 0 and len(combi) == 0) or \
        (i != 0 and i >= combi[-1]):
        # 문제에서는 nums 요소의 조건으로 1~40을 제시하였으나,
        # 만일 0이 포함되면 무한 재귀가 발생할 수 있으므로,
        # 이를 대비하기 위한 코드 작성
            combi.append(i)
            total()
            combi.pop()
        
total()
print(result)
        