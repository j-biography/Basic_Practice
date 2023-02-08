
# 10807


'''
     
N = int(input())

nums = []

nums.extend(map(int, input().split()))

v = int(input())

print(nums.count(v))

'''


'''

N = int(input())
nums = []
nums.extend(map(int, input().split()))
count = 0
v = int(input())

for i in range(N):
     if nums[i] == v:
          count += 1
          
print(count)
     
''' 

'''

N = int(input())

nums = list(map(int, input().split()))

v = int(input())

print(nums.count(v))

'''

# 10871

'''

N, X = map(int, input().split())

A = list(map(int, input().split()))


for i in range(N):
     if A[i] < X:
          print(A[i], end = ' ')
          
          '''

# 10818

'''

N = int(input())

A = list(map(int, input().split()))

print(min(A), max(A))

''' # min, max 내장함수를 사용해서 구현

'''

N = int(input())
A = list(map(int, input().split()))

min = 10000000
max = -10000000

for i in range(N):
     if max <= A[i]:
          max = A[i]
     if min >= A[i]:
          min = A[i]
     
print(min, max)

''' # min, max 기능을 직접 생성하여 구현


# 2562

'''

check = 0
max = 0
list = []

for i in range(9):
     N = int(input())
     list.append(N)
     
     if N > max:
          max = N
     else:
          continue
          
# print(max, list.index(max)+1, sep='\n')
print(max)
print(list.index(max) +1)

'''

'''

A = []

for i in range(9):
     A.append(int(input()))

print(max(A))      
print(A.index(max(A))+1)

'''

# 5597

'''

num = []
list = []

for i in range(28):
     num.append(int(input()))
     
for j in range(1,31):
     if j not in num:
          print(j)

'''

# 3052

'''

Rest = []

for i in range(10):
     A = int(input())
     B = 42
     if A%B not in Rest:
          Rest.append(A%B)
     else:
          continue
          
print(len(Rest))

'''

# 1546

'''

# N = int(input())

# Score = list(map(int, input().split()))

# M = max(Score)

# Value = (Score[0]*100 + Score[1]*100 + Score[2]*100) / (M*3)

# print(round(Value, 5))

'''

'''

# N = int(input())

# Score = list(map(int, input().split()))

# M = max(Score)

# list = []

# for i in range(N):
#      list.append(Score[i]*100 / (M*N))
     
# print(sum(list))

'''

'''

N = int(input())

Score = list(map(int, input().split()))

M = max(Score)

sum = 0

for i in range(N):
     sum += (Score[i]*100 / (M*N))
     
print(sum)

'''


# 8958


'''
     
import re

T = int(input())

for i in range(T):
     string = input()
     string2 = re.findall('[O]+', string)
     count = 0
     
     for j in range(len(string2)):
          count += (len(string2[j])+1) * len(string2[j]) / 2

     print(int(count))
          
     '''

'''
     
T = int(input())

for i in range(T):
     
     N = input()
     list_N = list(N)
     
     sum = 0
     count = 1
     
     for j in range(len(list_N)):
          
          if list_N[j] == 'O':
               sum += count
               count += 1
          else:
               count = 1
               
     print(sum)
     
     '''
     
# 4344

import sys

C = int(sys.stdin.readline())

for i in range(C):
     # N = list(map(int, input().split()))
     N = list(map(int, sys.stdin.readline().split()))
     
     average = sum(N[1:]) / N[0]
     count = 0
     Sum = 0
     
     for j in range(N[0]):
          
          if N[j+1] > average:
               Sum += N[j+1]
               count += 1  
          
     value = (count / (len(N)-1)) * 100
          
     print(f'{value:0.3f}%')
    
               

     