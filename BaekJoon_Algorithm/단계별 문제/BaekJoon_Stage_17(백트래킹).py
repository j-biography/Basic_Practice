
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

# 2580(스도쿠)

# 무식한 방식 / 실패

'''
Arr = [list(map(int, input().split())) for i in range(9)]
# result = [[]*i for i in range(9)]

def sudoku():
    for i in range(9):
        if Arr[i].count(0) == 0: #가로줄 탐색
            continue
        
        for j in range(9):
            if Arr[i][j] != 0:
                continue
            
            elif Arr[i][j] == 0 and Arr[i].count(0) == 1:
                Arr[i][j] = 45 - sum(Arr[i])
            
            elif Arr[i][j] == 0 and Arr[i].count(0) >= 2:
                count = 0
                total = 0
                for k in range(9): # 세로줄 탐색
                    if Arr[k][j] == 0:
                        count += 1
                    elif Arr[k][j] != 0:
                        total += Arr[k][j]
                        
                if count == 1:
                    Arr[i][j] = 45 - total
                elif count >= 2:
                    count = 0
                    total = 0
                    x = i // 3
                    y = j // 3
                    for m in range(3): # 3X3 탐색
                        for n in range(3):
                            if Arr[(x*3)+m][(y*3)+n] == 0:
                                count += 1
                            elif Arr[(x*3)+m][(y*3)+n] != 0:
                                total += Arr[(x*3)+m][(y*3)+n]
                                
                    if count == 1:
                        Arr[i][j] = 45 - total
                    elif count >= 2:
                        continue
    
    for i in range(9):
        if Arr[i].count(0) != 0:
            sudoku()
            return
        
    for j in range(9):
        for k in range(9):
            print(Arr[j][k],end=' ')
        print('')       
                    
sudoku()
'''

# 엘레강스한 DFS(백트래킹) 재귀 구현
'''
Arr = [list(map(int, input().split())) for i in range(9)]
zero = [(i, j) for i in range(9) for j in range(9) if Arr[i][j] == 0]

def check(i, j):
    nums = [1,2,3,4,5,6,7,8,9]
    
    
    for k in range(9):
        if Arr[i][k] in nums:
            nums.remove(Arr[i][k])
        if Arr[k][j] in nums:
            nums.remove(Arr[k][j])
    
    # if len(nums) == 1:
    #     return nums
    
    x = i // 3
    y = j // 3
    
    for a in range(3):
        for b in range(3):
            if Arr[(x*3)+a][(y*3)+b] in nums:
                nums.remove(Arr[(x*3)+a][(y*3)+b])
                    
    return nums

answer = False
def dfs(x):
    global answer
    
    if answer:
        return 
    
    if x == len(zero):
        for row in Arr:
            print(*row)
        answer = True
        return
    
    else:
        (i, j) = zero[x]
        nums = check(i, j)
        
        for num in nums:
            Arr[i][j] = num
            dfs(x+1)
            Arr[i][j] = 0
    
dfs(0)'''


# 바로 위 코드 톺아보면서 정리 & 이해한되는 부분 숙지(시간초과)

import sys
input = sys.stdin.readline

Sudoku = [list(map(int, input().split())) for i in range(9)]
zero = [(i, j) for i in range(9) for j in range(9) if Sudoku[i][j] == 0]

def check(i, j):
    nums = [1,2,3,4,5,6,7,8,9]
    
    for k in range(9):
        if Sudoku[i][k] in nums:
            nums.remove(Sudoku[i][k])
        if Sudoku[k][j] in nums:
            nums.remove(Sudoku[k][j])
     
    x = i // 3
    y = j // 3
    
    for a in range(x*3, (x+1)*3):
        for b in range(y*3, (y+1)*3):
            if Sudoku[a][b] in nums:
                nums.remove(Sudoku[a][b])
                
    return nums

def dfs(x):
    
    if x == len(zero):
        for i in Sudoku:
            print(*i)
        return
    
    (i, j) = zero[x]
    nums = check(i, j)
    
    for num in nums: # 정답이 아니더라도 후보군을 일단 넣고, 끝까지 가본다. 
        Sudoku[i][j] = num
        dfs(x+1)
        Sudoku[i][j] = 0
            
dfs(0)
    
                
            
    





            

        
        
        
    
            