list_2d_1 = [ [2,-2], [5,3] ]
list_2d_2 = [ [-1, 4], [7,-6] ]
list_answer = []

for i in range(len(list_2d_1)):
    temp = []
    for j in range(len(list_2d_1[i])):
        temp_multi = 0
        for k in range(2):
            temp_multi += list_2d_1[i][k]*list_2d_2[k][j]
        temp.append(temp_multi)
    list_answer.append(temp)

print(list_answer)