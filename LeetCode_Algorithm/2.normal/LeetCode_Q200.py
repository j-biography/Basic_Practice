
# Q.200
# 1을 육지로, 0을 물로 가정한 2D 그리드 맵이 주어졌을 때, 섬의 개수를 계산하라.
# 그리드 맵은 M X N 크기로 주어진다.

# dfs 함수를 만들어, 전체 맵을 탐색하면서 1을 발견하면, 
# 동서남북 4방면을 재탐색 반복하면서 섬을 이루는 덩어리를 찾아내는 방법.

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
   
def dfs(grid, i, j):
    if grid[i][j] == 1:
        grid[i][j] = 0
        island += 1
        dfs(grid, i+1, j)
        dfs(grid, i-1, j)
        dfs(grid, i, j+1)
        dfs(grid, i, j-1)
    else:
        return

island = 0  

for i in range(len(grid)):
    for j in range(len(grid[i])):
        dfs(grid, i, j)
        
print(dfs(grid, i, j))
        
    