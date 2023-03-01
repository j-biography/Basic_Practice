
# Q.200
# 1을 육지로, 0을 물로 가정한 2D 그리드 맵이 주어졌을 때, 섬의 개수를 계산하라.
# 그리드 맵은 M X N 크기로 주어진다.

# dfs 함수를 만들어, 전체 맵을 탐색하면서 1을 발견하면, 
# 동서남북 4방면을 재탐색 반복하면서 섬을 이루는 덩어리를 찾아내는 방법.    
# 코드 여러줄로 나누어 작성하는 방법 -> 괄호안에 넣거나 \(백슬래시)를 사용한다.

input_grid = [["1","1","1"],
              ["0","1","0"],
              ["1","1","1"]]
  

def dfs(grid, i, j):
     # i 혹은 j가 외곽을 넘었거나 grid[i][j]가 1이 아닌경우를 필터링한다.
    if i < 0 or \
        i >= len(grid) or \
        j < 0 or \
        j >= len(grid[0]) or \
        grid[i][j] != '1':
            return
    # 이미 확인한 땅(1)은 중복 계산 방지를 위해 0으로 변경해준다.
    grid[i][j] = '0'
        
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)
    
def island(grid):
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
                
    return count

print(island(input_grid))