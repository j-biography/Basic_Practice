
# 15649

# DFS 백트래킹 방식으로 수열 생성(성공) - 책 방식 응용
'''
N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]
result = []

def dfs(nums, M):
    if len(result) == M:
        print(' '.join(list(map(str, result))))
        
    for n in nums:
        result.append(n)
        nums2 = nums.copy()
        nums2.remove(n)
        dfs(nums2, M)
        result.pop()
        
dfs(nums, M)
'''

# 다른 유저 풀이법 학습 - 매우 심플 / 함수에 매개변수가 필수적으로 들어가지 않아도 된다는 것 학습.
'''
N, M = map(int, input().split())
result = []

def dfs():
    if len(result) == M:
        print(' '.join(list(map(str, result))))
        return
        
    for i in range(1, N+1):
        if i not in result:
            result.append(i)
            dfs()
            result.pop()
            
dfs()
'''


# 15650

# DFS(백트래킹) 방식으로 '오름차순'으로 이루어진 수열 생성
'''
N, M = map(int, input().split())
result = []

def dfs():
    if len(result) == M:
        print(' '.join(list(map(str, result))))
        
    for i in range(1, N+1):
        
        if len(result) == 0 or \
        (i not in result and \
        i > result[-1]):
            
            result.append(i)
            dfs()
            result.pop()
            
dfs()
'''

# 15651

# 같은 수를 여러번 골라도 되는 모든 수열 생성
'''
N, M = map(int, input().split())
result = []

def dfs():
    if len(result) == M:
        print(' '.join(list(map(str, result))))
        return 
        # return문을 넣어주지 않으면 바로 for 문으로 내려가서 불필요한 append 실행
    
    for i in range(1, N+1):
        result.append(i)
        dfs()
        result.pop()
        
dfs()
'''

# 15652

# 같은 수를 여러번 골라도 되며, 비내림차순인 모든 수열 생성
'''
N, M = map(int, input().split())
result = []

def dfs():
    if len(result) == M:
        print(' '.join(list(map(str, result))))
        return
    
    for i in range(1, N+1):
        if len(result) == 0 or \
        i >= result[-1]:
            
            result.append(i)
            dfs()
            result.pop()
            
dfs()
'''

# 9663






            

        
        
        
    
            