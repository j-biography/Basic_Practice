
##### 사전 연습 문제 알고리즘 - 1
'''
# 배열 nums 내의 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하라.
# nums에 들어있는 숫자의 개수는 5개 이상 50개 이하이며,
# nums의 각 원소는 1이상 1000이하의 자연수이고, 중복된 숫자는 들어있지 않다.
'''

# 브루트 포스(3-point)로 모든 조합을 구하고, 소수인지 판별.
'''
nums = [1,3,5,7,9,10]
prime = 0 # 소수의 개수

# 조합 생성
for i in range(len(nums)-2):
    for j in range(i+1, len(nums)-1):
        for k in range(j+1, len(nums)):
            total = nums[i]+nums[j]+nums[k]
            
            # 소수 판별
            for l in range(2, total+1):
                if total != l and total % l == 0: 
                    break
                elif l == total:
                    prime += 1
    
print(prime)'''


# itertools 라이브러리를 사용하여 모든 조합을 구하고, 소수인지 판별.
'''
from itertools import combinations

nums = [1,3,5,7,9,10]
prime = 0 # 소수의 개수

# 조합 생성
l = list(combinations(nums,3))

# 소수 판별
for i in l: # 숫자 3개 조합
    for j in range(2, sum(i)+1):
        if sum(i) != j and sum(i) % j == 0:
            break
        elif sum(i) == j:
            prime += 1

print(prime) '''


##### 본 테스트 문제 알고리즘 - 1
'''
Level(경사로 단계), Height(적설량)이 LH = [3,1,4,10,1] 등의 형태로 주어진다. 
경사로는 단계별로 (n*2)+1의 눈을 버틸 수 있다.
5단계의 경사로가 주어진다면, 이 경사로는 단계별로 각각 [1,3,5,7,9] 만큼의 눈의 양을 버틸 수 있다.
5단계의 경사로에 [3,1,4,10,1]의 눈이 내린다면, 각 경사 단계가 버틸 수 있는 정도까지 쌓이고 남은 눈은 다음 경사로로 넘어간다.
이 경우 경사로에 쌓인 눈을 출력하라. > [1,3,4,7,4]
'''
'''
LH = [0,1,4,10,1,9] # >> [0,1,4,7,4,9]

# 경사로는 5단계에 국한되어있지 않다. 
# LH[i] 는 (i*2)+1 을 제외한 값을 다음 경사로로 리턴한다.

rest = 0 # 남은 눈
result = []

for i in range(len(LH)):
    if ((LH[i]+rest) - ((i*2)+1)) > 0:
        result.append((i*2)+1)
        rest = ((LH[i]+rest) - ((i*2)+1))
    else:
        result.append(LH[i]+rest)
        rest = 0

print(result)'''


##### 본 테스트 문제 알고리즘 - 2
'''
여러 선분들의 시작점, 끝점(x1, y1, x2, y2)으로 이루어진 좌표 정보 N개가 제공된다.
이 선분들이 좌표평면에 놓아졌을 때, 십자 모양을 이루는 경우 십자 모양의 크기 MAX(십자를 이루는 선분의 절반 길이)를 출력하라.
단 십자 모양을 이루는 선분이 다른 선분에 의해 가로막힐 경우(90도), 가로막혀진 지점까지만 십자 모양으로 인정된다.
십자 모양이 없을 경우엔 -1을 출력하라.
'''




##### 본 테스트 문제 알고리즘 - 3
# 25972와 유사
'''
여러 도미노 블록들이 Position(위치), Height(높이) 값을 가지고 주어진다.
Position이 1이고, Height이 3인 도미노 블록[1,3]은 쓰러지면 Position 2,3,4에 있는 블록까지 무너뜨린다.
제거할 수 있는 도미노 블록 수 M이 주어질 때, 가장 위험한 블록 M개를 뺀 후에도 무너지게 되는 최소한의 블록 개수를 출력하라.
'''


PH = [[1,10],[3,10],[5,1],[9,4],[13,1]] # 1개만 빼면 반드시 최소 4개가 무너지는 TestCase 
M = 1

l = []
l_count = []

# PH의 개수에서 M을 뺐을 때 가능한 조합 = PH! / (PH-M)! * M!
# 백트래킹 재귀로 모든 조합별 최대 파괴되는 도미노의 수를 산출

def dfs():
    if len(l) == len(PH)-M:
        count = 1
        rest = 0
        for i in range(len(l)-1):
            if max(rest, sum(l[i])) >= l[i+1][0]:
                rest = max(rest, sum(l[i]))
                count += 1
        l_count.append(count)
        return
    
    for num in PH:
        if len(l) == 0 or (num[0] > l[-1][0] and num not in l):
            l.append(num)
            dfs()
            l.pop()

dfs()
print(min(l_count))
    


##### 본 테스트 문제 알고리즘 - 4
'''
# 손님의 수와 젓가락 짝이 리스트 = [AA, BC, BD, CD] 등의 형태로 주어진다.
# 손님은 자기 바로 옆 손님과 젓가락 하나만을 교환할 수 있을 때, 
# 모두가 짝이 맞는 젓가락을 가지기 위해 해야하는 최소 교환 횟수 N을 출력하라.
'''

# 삽입 정렬로 해결
'''
chop = ['CA','BD','BA','CD'] # [3,1],[2,4],[2,1],[3,4]
N = len(chop)
new = [[]*i for i in range(N)]
count = 0

for i in range(N):
    for j in range(2):
        new[i].append(ord(chop[i][j])-64)
    
for i in range(N):
    if new[i][0] == new[i][1]:
        continue
    else:
        max(new[i][0],new[i][1]), min(new[i+1][0],new[i+1][1])
        '''
        
# 정렬로 해결(무조건 가장 가까운 조합부터 변경)
'''
chop = ['CA','BD','BA','CD']
N = len(chop)
new = [[]*i for i in range(N)]

for i in range(N):
    for j in range(2):
        new[i].append(ord(sorted(chop[i])[j])-64)
        
for i in range(N):
    if new[i][0] == new[i][1]:
        continue
    for j in range(N):
        if new[i+j][1] == new[i+j+1][0]:
            '''
    
            


##### 본 테스트 문제 SQL - 1
'''
테이블 A에서 고객의 ID 컬럼을 출력해야한다.
고객의 ID 정보는 영문+숫자 조합으로 이루어져 있는데 ( ex. myid23, new007 )
이를 영문+숫자4자리 형태로 통일시켜야 한다. ( ex. myid0023, new0007)
숫자 앞에 0을 붙여 형태를 통일한 뒤 ID 컬럼을 출력하라.
'''

# SELECT 

# CONCAT(REGEX_SUBSTR(ID, '[A-Z]+'),LPAD(REGEX_SUBSTR(ID, '[0-9]+'), 4, 0))

# FROM A

