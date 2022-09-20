def insertion_sort(nums, how_many_nums):
    for index in range(1, how_many_nums):
        for j_index in range(index, 0, -1):
            if nums[j_index] < nums[j_index - 1]:
                nums[j_index], nums[j_index - 1] = nums[j_index - 1], nums[j_index]
            else:
                break

    return nums


numbers = [-3, 5, 0, 8, 1, 10]
length = len(numbers)
sorted_numbers = insertion_sort(numbers, length)
print(sorted_numbers, numbers)
