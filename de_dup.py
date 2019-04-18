list_with_duplicates = [1,2,3,4,4,2,3,4,5]
unique_list = []

for i in range(len(list_with_duplicates)):
    count = 0
    for j in range(len(list_with_duplicates)):
        if list_with_duplicates[i] == list_with_duplicates[j]:
            count += 1
    if count == 1:
        unique_list.append(list_with_duplicates[i])

print('Original list: %s' % list_with_duplicates)
print('Unique list: %s' % unique_list)