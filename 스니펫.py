
# 1. 문자열 뒤집기(Reverse string)
# 문자열 자체를 뒤집는 건 reversed()
# 배열의 순서를 뒤집는 건 .reverse()

string = 'abcde'

reversed_string = string[::-1]

print(reversed_string)


# 2. 첫번째 글자 대문자 변환(Capitalize 1st letter)
# title() 메서드를 활용하여 첫 글자만 대문자로 변환가능.
# upper() 메서드는 문자열 전체를 대문자로, lower() 메서드는 소문자로 변환.

string = 'abcde' # title() 메서드를 사용하여 간편하게

upper_string = string.title()

print(upper_string)


string = 'abcde' # replace() 메서드로 치환도 가능

upper_string = string.replace(string[0], string[0].upper())

print(upper_string)


# 3. 문자열에서 중복 요소 제거(Eliminate duplicated letter)
# set() 메서드를 사용하여 문자열의 중복 요소 제거 후
# ''.join() 메서드로 리스트(set)화 되어 있는 문자열을 다시 합침

string = 'abcabcabc'

set_string = ''.join(sorted(set(string)))

print(set_string)


# 4. 문자열 또는 리스트 반복 출력(Repeating output string or list)

string = 'abc'
l1 = ['a','b','c']
n = 5

print(string*n)
print(l1*n)


# 5. 리스트 내포(List Comprehension)

l1 = [1,2,3,4,5]
l2 = [10,20,30,40,50]

new_l = [i+j for i in l1 for j in l2 if l1.index(i) == l2.index(j)]

print(new_l)


# 6. 두 변수 값 서로 바꾸기(Exchange Value)

a = 1
b = 2

a, b = b, a

print(a, b)


# 7. 문자열 나누기(Split string)
# 8. 문자열 합치기(Join string)

string1 = 'Do the Right Thing. To the Right Way.'
string2 = string1.split()
string3 = ''.join(string2)
print(string3)


# 9. 회문 확인(Check Palindrome)

string = 'abbaabba'

if string == string[::-1]:
    print('right')
else:
    print('wrong')
    
    
# 10. 요소 개수 세기(Count elements)
# 기본적인 count() 메서드로 찾는 요소의 개수를 하나씩 리턴받을 수도 있지만
# collections 라이브러리의 Counter 메서드를 사용하면 모든 요소의 개수를 딕셔너리로 리턴받을 수 있다.
# most_common() 메서드 사용시 최빈값을 별도로 추출 가능하다.

from collections import Counter

string = 'abckjkeeeijd'

string_dict = Counter(string)
most_3 = string_dict.most_common(3)

print(string.count('a'))
print(string_dict)
print(most_3)


# 11. 애너그램 판별(Check Anagram)
# collections 라이브러리를 사용하여, 문자열 내부의 요소(키, 밸류)값이 같은지 대조

from collections import Counter

string1 = 'Le sserafim'
string2 = 'Im fearless'

string1_dict = Counter(string1.lower())
string2_dict = Counter(string2.lower())

if string1_dict == string2_dict:
    print('Le SSERAFIM')
else:
    print('Re SSERAFIM')
    

# 12. 오류 예외 처리(Ignore Error Message)
# Try / Except / Else / Finally
# Try & Except 구문은 기본적인 예외처리문이다.
# Else 절을 더하면, 오류가 발생하지 않을시의 행동을 지시할 수 있다.
# Finally 절을 더하면, 오류 발생 여부와 관련없이 반드시 마지막에 할 행동을 지시할 수 있다.


a, b = 1, 0

try:
    a/b
except ZeroDivisionError:
    print('division by zero')
else:
    print(a/b)
finally:
    print(('finally always run'))
    

# 13. Enumerate(열거) 메서드로 딕셔너리 제작(Use Enumerate Method)

l = ['a','b','c','d','e']

l2 = enumerate(l) # 딕셔너리 타입

for idx, value in l2:
    print(idx, value)
    
    
# 14. 메모리 사용량 확인(Check object's memory usage)

import sys

l = [1,2,3,4,5]
string = 'abc'
num = 7

print(sys.getsizeof(l))
print(sys.getsizeof(string))
print(sys.getsizeof(num))


# 15. 딕셔너리 병합
# update() 방식 / 연산자(**) 사용 방식 / 연산자(|, |=) 사용 방식

    # 1번 방식. update() 메서드를 활용하여 병합한다. 새 딕셔너리를 반환해주지 않는다.
dict1 = {'a':2, 'b':3, 'c':5}
dict2 = {'a':7, 'x':4, 'y':1}

dict1.update(dict2)
print(dict1)

    # 2번 방식. **(kargs)연산자 사용시 함수에 바로 넣을 수 있어서 간편하다.
dict3 = {'a':2, 'b':3, 'c':5}
dict4 = {'a':7, 'x':4, 'y':1}

print({**dict4, **dict3})

    # 3번 방식. 파이썬 3.9 이상 버전에서 추가된 연산자.
dict6 = {'a':2, 'b':3, 'c':5}
dict7 = {'a':7, 'x':4, 'y':1}
dict8 = {'a':10, 'b':10, 'x':10}

dict6|dict7 #병합
dict6|=dict8 # 업데이트

print(dict6)


# 16. 코드 실행 시간(Time to execute the code)

import time

start = time.time()

a,b = 0,1
a,b = b,a
print(a,b)

end = time.time()

runtime = end-start
print(runtime)


# 17. 이중 리스트, 삼중 리스트를 분해(Flattening list)
# 다만, 파이썬 내장 라이브러리가 아니다.

import iteration_utilities

l = [[1,2,3],[1],[1,2,[2,3,4]]]

print(list(iteration_utilities.flatten(l))) # 한단계 깊이만 풀어줌
print(list(iteration_utilities.deepflatten(l, depth=5))) # 원하는만큼 깊게 풀어줌


# 18. 랜덤(Random)
# 암호화시에는 Secrets 모듈 사용을 권장

import secrets
import random

l = [1,2,3,4,5]
l2 = random.sample(l,1)
l3 = secrets.SystemRandom().choice(l)

print(l2)
print(l3)


# 19. 숫자 나누기(Digitize)

num = 12345

print(list(str(num))) # Str 형식으로 숫자가 리스트에 저장
print(list(map(int, str(num)))) # Int 형식으로 리스트에 저장
print([int(x) for x in str(num)]) # 리스트 내포 방식으로 상기 구문 변형


# 20. 중복 요소 유무 확인

l = [1,2,3,4,5,5,6]
l2 = set(l)

if len(l) == len(l2):
    print('unique')
else:
    print('duplicated')
    