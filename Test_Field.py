# N = input()

# print(N[0])
# print(N[1])

# print(int(N))

# N = input()

# a = int(N)
# b = str(a)

# print(b[0])

# print(list(range(1,3)))

# for i in range(5):
#     print(i)

# print(max(2, 4))

# dots = [[1,4],[9,2],[3,8],[11,6]]

# print(dots[0],dots[1])



# 피보나치랑 팩토리얼이랑 헷갈려서 이런 괴이한 코드 작성.(반성)
'''
def factorial(n):
    if n < 2:
        return n
    else:
        return factorial(n-2) + factorial(n-1)

print(factorial(30))
'''

'''
n = 10
sum = 1

for i in range(1,n+1):
    sum *= i
    
print(sum)
'''

# 파이썬 알고리즘 테스트 - 12장 그래프 탐색 

# 그래프 A가 있을 때, 정점을 모두 방문하는 루트를 DFS / BFS

l = [1,2,0,0,0,0,3,4,5]

print(l.pop())
print(l.pop(3))
