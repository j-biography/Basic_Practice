

# 그리디 알고리즘
# 정렬

# N = 도미노의 개수, a1 = 도미노의 좌표, l1 = 도미노의 길이가 주어진다.

import sys
input = sys.stdin.readline

N = int(input())
# domino = [list(map(int,input().split())) for i in range(N)]
domino = sorted([list(map(int,input().split())) for i in range(N)], key = lambda x:x[0])
count = 0
    
for i in range(N-1):
    if domino[i][0]+domino[i][1] < domino[i+1][0]:
        count += 1
    else:
        continue
    
print(count+1)


# 이를 응용하여 SM_14th_1 의 3번 알고리즘 문제 PS


        