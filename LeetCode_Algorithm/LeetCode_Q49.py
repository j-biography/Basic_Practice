# Q49. 그룹 애너그램

import collections

anagrams = collections.defaultdict(list)

A = ['eat','tea','tan','ate','nat','bat']

for word in A:
    anagrams[''.join(sorted(word))].append(word)
    
print(anagrams.values())

# print(sorted('dkwerwaafj'))
# print(''.join(sorted('dkwerwaafj')))