list_numbers = [-1,-2,-3,1,2,3,4,5,6,7]
positive_numbers = []

for i in range(len(list_numbers)):
    if list_numbers[i] > 0:
        positive_numbers.append(list_numbers[i])

print(positive_numbers)