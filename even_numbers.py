list_numbers = [1,2,3,4,5,6,7,8,9,10]
evens = []

for i in range(len(list_numbers)):
    if list_numbers[i] % 2 == 0:
        evens.append(list_numbers[i])

print(evens)