
a = [1,2,3,4,5,6,7,8,9]

def solve(a):
    ans = 0
    
    for i in range(len(a)):
        if len(a[i]) > 1:
            for j in range(len(a[i])):
                ans += a[i][j]
                if len(a[i][j]) == 1:
                    continue
                else:
                    print('break')
        else: 
            ans += a[i]
    
    print(ans)
    return ans
    
solve(a)

# a = [1,2,3,4,5]

# for i in range(a):
#     b = sum(a[0:])

# print(b)
     