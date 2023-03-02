
# Q.77

# 전체 정수 N개를 입력받아 K개로 이루어진 조합을 출력하라.

# 백준 15649번 문제 풀이 응용
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        l = []

        def dfs():
            if len(l) == k:
                result.append(l.copy())
                return

            for i in range(1, n+1):
                if len(l) == 0 or \
                (i not in l and 
                i >= l[-1]):

                    l.append(i)
                    dfs()
                    l.pop()

        dfs()
        return result
        '''
        
# 알고리즘 인터뷰 책.Ver
'''
def combine(N, K): # N과 K는 각각 주어지는 정수의 범위와, 조합 가능한 수의 개수를 의미한다.
    result = []
    l = []
    
    def dfs(start, K):
        if K == 0:
            result.append(l.copy())
            return
        
        for i in range(start, N+1):
            l.append(i)
            dfs(start+1, K-1)
            l.pop()
            
    dfs(1, K)
    print(result)
    
combine(4, 2)
'''
        

        
        


