
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



    
        


    
    