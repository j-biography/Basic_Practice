

arr = [1,2,3,3,3,4]

count_list = [0] * (max(arr)+1)

for i in arr:
    count_list[i] += 1


if count_list.count(max(count_list)) == 1:
    print(count_list.index(max(count_list)))
else:
    print(-1)

# print(count.index(max(count_list)))