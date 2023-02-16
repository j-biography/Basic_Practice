
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
# 시간초과
'''
import sys
input = sys.stdin.readline

N = int(input())
l = [int(input()) for i in range(N)]

def average(l):
    print(int(round(sum(l)/len(l),0)))

def middle(l):
    print(int(sorted(l)[len(l)//2]))

def frequency(l):
    if len(l) == 1:
        l2 = [0] * (max(l)+1)
    else:
        l2 = [0] * (max(l)+1-min(l))

    if min(l) < 0:
        for num in l:
            l2[num+abs(min(l))] += 1

        if l2.count(max(l2)) > 1:
            print(int(l2.index(max(l2), 2)-abs(min(l))))
        else:
            print(int(l2.index(max(l2))-abs(min(l))))

    else:
        for num in l:
            l2[num] += 1

        if l2.count(max(l2)) > 1:
            print(int(l2.index(max(l2), 2)))
        else:
            print(int(l2.index(max(l2))))

def range(l):
    print(int(max(l)-min(l)))

average(l)
middle(l)
frequency(l)
range(l)
'''

# 미리 리스트를 다 만들어놓고, 한번에 필요한 데이터를 가져오기.
# 위의 코드는 매번 데이터를 가져오기 위해 4번 반복을 수행했다.
# 왜 계속 틀리는걸까. 50~60%에서 계속 오답처리 됨. round를 바꿔봤으나 변경 X
'''
import sys
input = sys.stdin.readline

N = int(input()) # N = len(l)
l = []
l_cnt = [0] * ((4000*2)+1)
sum = 0

for i in range(N):
    num = int(input())
    l.append(num)
    sum += num
    l_cnt[num] += 1
    
l2 = sorted(l)

if l_cnt.count(max(l_cnt)) == 1: # 최빈값이 하나일 때
    max_freq = l_cnt.index(max(l_cnt))
    if max_freq > 4000: # 최빈값이 하나이며 음수일 때
        max_freq = -(8001-max_freq) # 인덱스 조정
else: # 최빈값이 두 개 이상일 때
    max_freq = l_cnt.index(max(l_cnt)) # 최빈값 중 하나만 음수일 때
    if l_cnt[4001:8001].count(max(l_cnt)) >= 2: # 최빈값 중 두 개 이상이 음수일 때
        l_cnt.remove(l_cnt[max_freq])
        max_freq = -(8001-l_cnt.index(max(l_cnt)))+1
    elif l_cnt[4001:8001].count(max(l_cnt)) == 0: # 최빈값이 모두 양수일 때
        l_cnt.remove(l_cnt[max_freq])
        max_freq = l_cnt.index(max(l_cnt))+1

# 첫째줄 - 평균(첫째 자리 반올림)
print(round((sum/N))) # round 함수의 특징을 공부할 것!
# 둘째줄 - 중앙값
print(l2[N//2])
# 셋째줄 - 최빈값
print(max_freq)
# 넷째줄 - 범위
print(l2[-1]-l2[0])
'''

# 최종 정답 = 깔끔, 그러나 최빈값을 collections 라이브러리로 구한 것이 못내 아쉽다.
'''
import sys
import collections
input = sys.stdin.readline

N = int(input())
l = sorted([int(input()) for i in range(N)])

frequency = collections.Counter(l).most_common()
if len(frequency) == 1: # 만약 문제에서 주어진 숫자가 1개 뿐인 경우
    max_freq = frequency[0][0]
else:
    if frequency[0][1] == frequency[1][1]: # 1순위 최빈값과 2순위 최빈값의 수량이 같다면
        max_freq = frequency[1][0]
    else:
        max_freq = frequency[0][0]

# 첫째줄 : 평균
print(round(sum(l)/N))
# 둘째줄 : 중앙값
print(l[N//2])
# 셋째줄 : 최빈값
print(max_freq)
# 넷째줄 : 범위
print(l[-1]-l[0])
'''

# 마침내 성공. collections 라이브러리를 사용하지 않고 코딩.

'''
import sys
input = sys.stdin.readline

N = int(input())
l = sorted([int(input()) for i in range(N)])

l_count = {}
l_most = []

for num in l:
    # key가 딕셔너리 내부에 없다는 가정하에, 
    # 딕셔너리[key] 구문을 사용하면 에러가 발생하지만, 
    # 딕셔너리.get(key) 구문은 None을 리턴한다.
    if l_count.get(num) is None: 
        l_count[num] = 1
    else:
        l_count[num] += 1
        
most = max(l_count.values())

# 키가 있으면 밸류를 알 수 있지만, 밸류만으로 키를 얻어낼 수 없다.
# 딕셔너리의 키:밸류를 뒤집어, 찾는 밸류값이
# 딕셔너리 내부에 있는지 확인하는 구문.
for key, value in l_count.items():
    if value == most:
        l_most.append(key)
        
if len(l_most) > 1:
    frequency = sorted(l_most)[1]
else:
    frequency = l_most[0]
    
    
# 첫째줄 : 평균
print(round(sum(l)/N))
# 둘째줄 : 중앙값
print(l[N//2])
# 셋째줄 : 최빈값
print(frequency)
# 넷째줄 : 범위
print(l[-1]-l[0]) 
'''

# 1427
'''
import sys
input = sys.stdin.readline

N = sorted(list(str(int(input()))),reverse = True)

print(''.join(N))
'''

# 11650

import sys
input = sys.stdin.readline

N = int(input())
l = []

for i in range(N):
    a,b = map(int, input().split())
    l.append([a,b])
    
l.sort(key = lambda x: (x[0],x[1]))

for i in range(N):
    print(l[i][0], l[i][1])

