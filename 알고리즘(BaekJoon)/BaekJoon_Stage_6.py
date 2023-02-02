
# 11654

# ord() 메서드 - 파이썬의 기본 내장 함수
# 문자를 입력받아, 유니코드/아스키코드 숫자 값을 리턴한다.

# chr() 메서드 - 파이썬의 기본 내장 함수
# 유니코드 숫자값을 입력받아, 이에 해당되는 문자(원문)값을 리턴한다.

'''
ex)

print(ord('a'))
print(chr(97))

'''

# 1번 방법
# print(ord(str(input())))

# 2번 방법
# a = str(input())
# print(ord(a))


# 11720

'''
N = int(input())
x = str(input())
count = 0

for i in range(N):
    count += int(x[i])
    
print(count)
'''

'''
N = int(input())
x = str(input())
a = []

for i in range(len(x)):
    a.append(int(x[i]))
    
print(sum(a))    
'''

# 10809

# index 기능으로 위치를 찾아낼 것

'''
s = input()

s_list = list(s)

alphabet = ['a','b','c','d','e',
            'f','g','h','i','j',
            'k','l','m','n','o',
            'p','q','r','s','t',
            'u','v','w','x','y','z']

for i in alphabet:
    if i in s_list:
        print(s_list.index(i), end=' ')
    else:
        print('-1', end=' ')
        '''
    
# find 함수는 찾는 값이 없을 경우 -1을 출력하는 것을 활용.
    
'''
s = input()

for i in range(97, 123):
    print(s.find(chr(i)), end=' ')
    '''
    
# 2675

'''
T = int(input())

for test_case in range(T):
    
    R, S = input().split()
    
    for repeat in range(len(S)):
        print(S[repeat]*int(R), end='')
    print()
    '''
    
# 1157

# 1차 코딩 실패 ver.

'''
voca = input().upper()
voca_list = []
count_value = 0

for i in range(len(voca)):
    voca_list.append(ord(voca[i]))

voca_list2 = list(set(voca_list))

for j in range(len(voca_list2)):
    value = voca_list.count(voca_list2[j])
    if value >= count_value:
        count_value = value 
    
print(count_value)
'''

# 완성하였으나 복잡. 코딩에 과도한 시간 소요되었으며, 런타임도 1000ms 이상. 복기해볼 것.

'''
N = input().upper()

a = []
b = []
count = 0
max = 0

for i in range(len(N)):
    a.append(ord(N[i]))
    if ord(N[i]) not in b:
        b.append(ord(N[i]))
        
for j in range(len(b)):
    if a.count(b[j]) > count:
        count = a.count(b[j])
        max = b[j]
    elif a.count(b[j]) == count:
        max = 63
    
print(chr(max))
'''

# 축약하여 2차 코딩 진행하였으나 런타임을 비약적으로 줄이지 못함.

'''
N = list(input().upper())

max = 0
check = 0

for i in range(65, 91):
    if N.count(chr(i)) > check:
        check = N.count(chr(i))
        max = chr(i)
    elif N.count(chr(i)) == check:
        max = '?'
        
print(max)
'''

# 3차 코딩. 획기적인 런타임 시간 단축. max값이 있는 위치(index)를 통해 최다 사용 알파벳을 역산출.

'''
N = input().upper()

a = []

for i in range(65, 91):
    a.append(N.count(chr(i)))

if a.count(max(a)) >= 2:
    print('?')
    
else:
    b = a.index(max(a))
    print(chr(65+b))
    '''

# 1152

'''
N = input().strip().split() 
# 입력받은 input 값의 앞/뒤 공백 제거 후, 공백을 기준으로 나누어 리스트 생성.

# N2 = set(N) 
# 중복값 제거
# 중복값 제거하면 안되는 조건을 나중에 확인.
# 조건은 두 번 세 번 꼼꼼하게 볼 것!

print(len(N))
# 단어 개수 카운트
'''

# 2908

'''
A, B = input().split()

A2 = int(A[::-1])
B2 = int(B[::-1])

if A2 > B2:
    print(A2)
else:
    print(B2)
'''

# 5622

# 단순한 방식
'''
N = input()
count = 0

for i in range(len(N)):
    if N[i] in ['A','B','C']:
        count += 3
    elif N[i] in ['D','E','F']:
        count += 4
    elif N[i] in ['G','H','I']:
        count += 5
    elif N[i] in ['J','K','L']:
        count += 6
    elif N[i] in ['M','N','O']:
        count += 7
    elif N[i] in ['P','Q','R','S']:
        count += 8
    elif N[i] in ['T','U','V']:
        count += 9
    elif N[i] in ['W','X','Y','Z']:
        count += 10

print(count)
    '''

'''
# 딕셔너리를 생성하여 내부에 {Key : Value}를 정리해두고 사용하는 방식.

N = input()
count = 0

data = { ('A','B','C') : 3,
         ('D','E','F') : 4,
         ('G','H','I') : 5,
         ('J','K','L') : 6,
         ('M','N','O') : 7,
         ('P','Q','R','S') : 8,
         ('T','U','V') : 9,
         ('W','X','Y','Z') : 10}

# 딕셔너리 내부엔 unhashable 타입 자료형인 리스트를 넣을 수 없어,
# unhashable 타입 자료형인 튜플을 넣음.

for key, value in data.items(): # 딕셔너리 내부 튜플(key)에 바로 접근이 불가하여, 딕셔너리를 한 번 풀어내 줌.
    for i in range(len(N)):
        if N[i] in key:
            count += data.get(key)
            
print(count)
'''

# 2941

# 정규표현식으로 시도
'''
import re

N = str(input())

N_list = (re.findall(r'c=|c-|dz=|d-|lj|nj|s=|z=|-|=|[a-z]', N))

print(len(N_list))
'''

#리스트로 리턴을 하면 한 글자로 쪼개준다는 것을 응용하여, 먼저 크로아티아 알파벳을 다 찾고 나머지는 쪼개버림.
'''
N = input()

Alpha = ['c=','c-','dz=','d-',
         'lj','nj','s=','z=']

for i in Alpha:
    N = N.replace(i, '.')

print(len(N))
'''

# 1316

'''
T = int(input())
count = T

for i in range(T):
    N = input()
    check = []
    for j in range(len(N)):
        if N[j] not in check:
            check.append(N[j]) 
        elif N[j] in check and N[j] != N[j-1]:
            count -= 1
            break

print(count)
'''

# 내가 눈으로 문제를 보고 푸는 방식을 노트에 기술한다.
# 이를 순차적으로 코드로 구현한다.

# 1. 주어지는 단어의 개수를 Count 값으로 지정한다.
# 2. Count 값만큼 테스트를 반복한다.
# 3. 단어 맨 앞부터 알파벳을 체크하며 뒤로 나아간다.
# 4. 이미 나온 알파벳이 뒤에 또 나오면 Break.
# 5. 다만 Break 전에 연속되는 경우인지 확인한다.
# 6. Break가 되면 Count값에서 1씩 차감한다.

    
        


    
    