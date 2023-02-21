
# 10872

# 팩토리얼 값을 for 문으로 구하기
# 정수 N이 주어질 때, N!값을 출력
'''
N = 10
sum = 1

for i in range(N, 0, -1):
    sum *= i
print(sum)
'''

# 팩토리얼 값을 재귀 함수로 구하기
'''
N = int(input())

def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)

print(factorial(N))
'''

# 10870

# 피보나치 수를 for 문으로 구하기
'''
N = int(input())

a, b = 0, 1

if N <= 1:
    print(N)
else:
    for i in range(1, N):
        a, b = b, a+b
    print(b)
'''

# 피보나치 수를 재귀 함수로 구하기
'''
N = 10
sum = 0

def fibo(x):
    global sum
    sum += 1
    if x <= 1:
        return x
    else:
        return fibo(x-1) + fibo(x-2)
    
print(fibo(N))
print(sum)
'''

# 피보나치 수를 DP - 하향식 - 메모이제이션으로 구하기
'''
dict = {}

def fibo(n):
    if n in dict:
        return dict[n]
    else:
        if n <= 1:
            return n
        dict[n] = fibo(n-2) + fibo(n-1)
        return dict[n]
    
print(fibo(10))
'''
# 피보나치 수를 DP - 상향식 - 타뷸레이션으로 구하기
'''
dict = {}

def fibo(n):
    for i in range(n+1):
        if i <= 1:
            dict[i] = i
        else:
            dict[i] = dict[i-2] + dict[i-1]
    return dict[n]
    
print(fibo(10))
'''

# 25501

# 문제와 관련없이 제작해본 팰린드롬 문자열 판별 코드
'''
N = int(input())

for i in range(N):
    string = input()
    l = len(string) 
    if string[0:l] == string[l::-1]:
        isPalindrome = 1
    else:
        isPalindrome = 0
        
print(isPalindrome)
'''

# (문제)재귀형 함수로 팰린드롬을 판별하고 판별 결과 & 함수 사용 횟수를 리턴

        # 문제에서 제공하는 C++ 힌트 코드 먼저 해석

'''
    include <stdio.h>   # C 프로그램에서 99% 이상 써놓고 시작하는 구문. stdio.h 헤더파일에는 입출력 기능 등이 내장되어있다.
    include <string.h>  # 문자열을 처리하는 헤더파일.

    int recursion(const char *s, int l, int r){ # isPalindrome 함수 내에서 recursion 함수를 사용하며,
        # 's(입력받은 문자열)', '0', 'len(s)-1'이 매개변수로 입력될 예정.
        if(l >= r) return 1;    # 만약 문자열이 한 글자로 이루어져 있거나, 나중에 l 값이 r 값 이상이 되는 경우 1 리턴 후 종료
        else if(s[l] != s[r]) return 0;     # 문자열 앞,뒤가 불일치 하는 경우, 0 리턴 후 종료
        else return recursion(s, l+1, r-1);     # 가운데로 좁혀들어가면서 계속 확인.
    }

    int isPalindrome(const char *s){
        return recursion(s, 0, strlen(s)-1);
    }

    int main(){
        printf("ABBA: %d\n", isPalindrome("ABBA")); // 1
        printf("ABC: %d\n", isPalindrome("ABC"));   // 0
    }
    '''
    
        # 파이썬 버전으로 번역되어 제공된 힌트 코드.
'''
    def recursion(s, l, r):
        if l >= r: return 1
        elif s[l] != s[r]: return 0
        else: return recursion(s, l+1, r-1)

    def isPalindrome(s):
        return recursion(s, 0, len(s)-1)

    print('ABBA:', isPalindrome('ABBA'))
    print('ABC:', isPalindrome('ABC'))
    '''

        # 최종적으로 제작한 정답 코드.
'''
    def recursion(s, start, end):
        global sum
        sum += 1
        
        if start >= end:
            return 1
        elif s[start] != s[end]:
            return 0
        else:
            return recursion(s, start+1, end-1)
        
    T = int(input())

    for i in range(T):
        sum = 0
        s = input()
        print(recursion(s, 0, len(s)-1), sum)
        '''




