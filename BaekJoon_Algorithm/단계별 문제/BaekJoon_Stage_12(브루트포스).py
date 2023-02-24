
# 2798

# itertools 라이브러리의 조합 메서드 combination()을 활용한 브루트포스
'''
import itertools

N, M = map(int, input().split())
card = [i for i in map(int, input().split())]
l = list(itertools.combinations(card, 3))
max = 0

for i in range(len(l)):
    if sum(l[i]) > max and sum(l[i]) <= M:
        max = sum(l[i])
    else:
        continue

print(max)
'''

# 파이썬 알고리즘 4부 - (DFS/BFS 그래프 탐색) 방식 활용

    # 가능한 모든 순열(permutation) 리턴
'''
def permute(nums):
    result = []
    prev_elements = []
    
    def dfs(elements):
        if len(elements) == 0:
            result.append(prev_elements[:])
        
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)
            
            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()
            
    dfs(nums)
    return result

print(permute([1,2,3]))
'''

    # 가능한 모든 조합(combination) 리턴
'''
def combine(nums, k):
    result = []
    l = []
    
    def dfs(nums, start, k):
        if k == 0:
            result.append(l[:])
            return
    
        for i in range(start, len(nums)+1):
            l.append(nums[i-1])
            dfs(nums, i+1, k-1)
            l.pop()
        
    dfs(nums, 1, k)
    return result

N = [1,2,3,4,5]
print(combine(N,2))
'''

    # 상기 코드를 응용하여 PS코드 작성
'''
N, M = map(int, input().split())

nums = [i for i in map(int, input().split())]

combi = [0]
new_combi = 0

def dfs(nums, i, k):
    global combi, new_combi
    limit = M
    if k == 0 and max(combi) < new_combi and new_combi <= limit:
        combi.pop()
        combi.append(new_combi)
        new_combi = 0
        return
    elif new_combi > limit:
        new_combi = 0
    
    for i in range(i, len(nums)+1):
        new_combi += nums[i-1]
        dfs(nums, i+1, k-1)
        
    return combi

print(dfs(nums, 1, 3))
'''

# 15649

N, M = map(int, input().split())

for i in range(N):
    for j in range(M,N):
        print(i, j)
        



        
    
    


    