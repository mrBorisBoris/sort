def bubble_sort(nums):
    length = len(nums)
    for count in range(length - 1):
        for index in range(length - 1):
            if nums[index] > nums[index + 1]:
                nums[index], nums[index + 1] = nums[index + 1], nums[index]
    return nums


numbers = [5, 7, 1, 4, 8]
print('Сортировка пузырьком: ')
print(bubble_sort(numbers))
