list_2d_1 = [ [1,3], [2,4] ]
list_2d_2 = [ [5,2], [1,0] ]
list_answer = []

for i in range(len(list_2d_1)):
    temp_added_list = []
    for j in range(len(list_2d_1[0])):
        temp_added_list.append( list_2d_1[i][j] + list_2d_2[i][j])
    list_answer.append(temp_added_list)

print(list_answer)