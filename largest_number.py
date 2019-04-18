list_numbers = [1,2,40,3,4,5,6]

max_number = 0

for i in range(len(list_numbers)):
    if list_numbers[i] > max_number:
        max_number = list_numbers[i]

print(max_number)

# The function below max() will search through the list and return the max number

#print(max(list_numbers))