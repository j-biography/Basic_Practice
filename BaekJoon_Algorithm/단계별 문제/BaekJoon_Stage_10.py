
# 2750
'''
N = int(input())
l = [int(input()) for _ in range(N)]

for i in sorted(l):
    print(i)
'''

# 2587
'''
n = [int(input()) for _ in range(5)]

def cal(n):
    avg = int(sum(n)/5)
    mid = sorted(n)[2]
    print(avg)
    print(mid)
    
cal(n)
'''

# 25305

'''
N, K = map(int, input().split())

score = [i for i in map(int, input().split())]

print(sorted(score)[-K])'''


# 2751

'''
import sys

N = int(sys.stdin.readline())

l = [int(sys.stdin.readline()) for i in range(N)]

for i in sorted(l):
    print(i)
'''

# 10989

# 계수 정렬(카운팅 정렬)로 코딩하였으나, 메모리 부족

'''

import sys

N = int(sys.stdin.readline())

l1 = [int(sys.stdin.readline()) for num in range(N)] # 원 배열

count = [0] * (max(l1)+1) # 요소 개수 저장 배열

for num in l1:
    count[num] += 1 # 원 배열 내부의 요소 개수를 세, count 배열 내부의 바른 위치에 저장

for num in range(1, len(count)):
    count[num] += count[num-1] # count 배열의 요소를 누적합으로 갱신
    
l2 = [0] * len(l1) # 최종 출력 배열

for num in l1:
    index = count[num]
    l2[index-1] = num
    count[num] -= 1

for i in l2:
    print(i)

'''

# 계수 정렬(카운팅 정렬)을 사용하면서, count 배열 내에 Constraint인 10000개를 채워둠.

'''
import sys

N = int(sys.stdin.readline())
count = [0] * 10000

for i in range(N):
    n = int(sys.stdin.readline())
    count[n-1] += 1
    
for i in range(10000):
    if count[i] != 0:
        for j in range(count[i]):
            print(i+1)
'''            
       
# sys.stdin.readline()을 반복 타이핑 하기 싫다면
# input = sys.stdin.readline으로 선언해두는 방법도 있다.

'''
import sys
input = sys.stdin.readline

N = int(input())
l1 = []

for i in range(N):
    n = int(input())
    l1.append(n)

count = [0] * (max(l1)+1)

for n in l1:
    count[n] += 1
 
for i in range(len(count)):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)
            '''

# 2108
import sys
input = sys.stdin.readline

N = int(input())
l = [int(input()) for i in range(N)]
l2 = [0] * (max(l)+1-min(l))

def average(l):
    print(round(sum(l)/len(l)), 1)

def frequency(l, l2):
    if min(l) < 0:
        for num in l:
            l2[num+abs(min(l))] += 1
            
        if l2.count(max(l2)) > 1:
            print(l2.index(max(l2), 2)-abs(min(l)))
        else:
            print(l2.index(max(l2))-abs(min(l)))
            
    else:
        for num in 1:
            l2[num] += 1
        
        if l2.count(max(l2)) > 1:
            print(l2.index(max(l2), 2))
        else:
            print(l2.index(max(l2)))

