

pattern = ['aya', 'ye', 'woo', 'ma']

babbling = ['ayaye', 'uuuma', 'ye', 'yemawoo', 'ayaa']
# babbling_join = ''.join(babbling)
babbling_2 = []
babbling_3 = []

for target_str in babbling:
    for check_str in pattern:
        if check_str in target_str:
            new_target_str = target_str.replace(check_str, ' ')
            target_str = new_target_str
            continue
    babbling_2.append(target_str)
    
for i in babbling_2:
    babbling_3.append(i.strip())
    
print(babbling_3.count(''))
    
