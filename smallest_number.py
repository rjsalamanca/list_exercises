list_numbers = [1,2,40,3,4,5,6]

min_number = 0

for i in range(len(list_numbers)):
    if i == 0:
        min_number = list_numbers[i]
    elif list_numbers[i] < min_number:
        min_number = list_numbers[i]

print(min_number)

# The method below min() will search through the list and return the smallest number

#print(min(list_numbers))