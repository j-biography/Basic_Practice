# 1. 유효한 팰린드롬


# 리스트 방식

def isPalindrome(s:str) -> bool:
    strs = []
    for char in s.lower():
        if char.isalnum():
            strs.append(char)
            
    while len(strs) > 1:
        if strs.pop(0) == strs.pop():
            continue
        else:
            print('False')

# 데크 방식

import collections

def isPalindrome(s:str) -> bool:
    strs = collections.deque()
    for char in s.lower():
        if char.isalnum():
            strs.append(char)
    
    while len(strs) > 1:
        if strs.popleft() == strs.pop():
            continue
        else:
            print('False')
            
# 슬라이싱 방식

import re

def isPalindrome(s:str) -> bool:
    s = s.lower
    
    s = re.sub('[^a-z0-9]', '', s)
    
    if s == s[::-1]:
        return True
    else:
        return False
