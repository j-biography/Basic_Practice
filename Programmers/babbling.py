pattern = ['aya', 'ye', 'woo', 'ma']

babbling = ['aya', 'yee', 'u', 'maa', 'wyeoo']
babbling_join = ','.join(babbling)
babbling_2 = []

for i in pattern:
    if i in babbling_join:
        new = babbling_join.replace(i,'')
babbling_2.append(new)
    
print(babbling_2)
        
            
            
# a = ['a','b','c']

# print(','.join(a))