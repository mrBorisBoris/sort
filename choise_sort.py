def choice_sort(nums):
    length = len(nums)
    for index in range(length - 1):
        for j_index in range(index + 1, length):
            if nums[index] > nums[j_index]:
                nums[j_index], nums[index] = nums[index], nums[j_index]
            else:
                continue
    return nums


print('Сортировка выбором: ')
numbers = [-2, 7, 8, 2, 1, 0]
sorted_numbers = choice_sort(numbers)
print(sorted_numbers)