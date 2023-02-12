# Q344. 문자열 뒤집기

# 파이썬의 내장 함수 사용

def reverseString(s):
    s = s.reverse()
    
# 투 포인터 구현

def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
