# Q5. 가장 긴 팰린드롬 문자열

def expand(left, right):
    while (left >= 0 and right < len(s) 
           and s[left] == s[right]):
        
        left -= 1
        right += 1
    return s[left+1 : right] # 바로 위에서 left / right 값을 조정하고 내려왔기 때문에.

###

s = str(input())

if len(s) < 2 or s == s[::-1]:
    print(s)
    
else:
    result = ''
    for i in range(len(s)-1):
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)
    
    print(result)