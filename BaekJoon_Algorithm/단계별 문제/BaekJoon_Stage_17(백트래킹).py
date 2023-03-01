
# 15649

# DFS 백트래킹 방식으로 조합(성공) - 책 방식 응용

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


# 다른 유저 풀이법 학습 - 매우 심플 / 함수에 매개변수가 필수적으로 들어가지 않아도 된다는 것 학습.

N, M = map(int, input().split())
result = []

def dfs():
    if len(result) == M:
        print(' '.join(list(map(str, result))))
        
    for i in range(1,N+1):
        if i not in result:
            result.append(i)
            dfs()
            result.pop()
            
dfs()
            


        
        
        
    
            