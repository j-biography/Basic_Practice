# Q819. 가장 흔한 단어
import re
import collections

paragraph = 'Bob hit a ball, the hit Ball.'

banned = 'hit'

words = [word for word in re.sub('[^\w]',' ',paragraph).lower().split() 
         if word not in banned]

print(collections.Counter(words).most_common(1)[0][0])

# count = collections.defaultdict(int)
# for word in words:
#     count[word] += 1
    
# print(max(count, key=count.get))
