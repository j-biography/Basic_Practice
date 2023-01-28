
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

#