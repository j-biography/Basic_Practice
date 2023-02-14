
# 2738
'''
N, M = map(int, input().split())

A_list = [list(map(int, input().split())) for _ in range(N)]
B_list = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        print(A_list[i][j] + B_list[i][j], end=' ')
    print()
    '''

# 2566
'''
A_list = [list(map(int, input().split())) for _ in range(9)]
count = 0
position = [0,0]

for i in range(9):
    for j in range(9):
        if A_list[i][j] >= count:
            count = A_list[i][j]
            position = [i+1,j+1]

print(count)
print(position[0], position[1])
'''

# 2563
'''
N = int(input()) # 종이의 수

paper = [[[0] for col in range(101)] for row in range(101)]

for i in range(N):
    a, b = map(int, input().split())
    for i in range(1,11):
        for j in range(1,11):
            paper[a+i][b+j] = 1
            
result = 0  
for i in paper:
    result += i.count(1)
    
print(result)
'''




        