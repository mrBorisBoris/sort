first, second = 4, 5
first_list = [2, 8, 8, 19]
second_list = [3, 4, 5, 5, 10]
result = []
i_index = j_index = 0

while i_index < first and j_index < second:
    if first_list[i_index] < second_list[j_index]:
        result.append(first_list[i_index])
        i_index += 1
    else:
        result.append(second_list[j_index])
        j_index += 1

while j_index < second:
    result.append(second_list[j_index])
    j_index += 1

while i_index < first:
    result.append(first_list[i_index])
    i_index += 1


print(*result)
