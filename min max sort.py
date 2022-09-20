import random


def min_sort(nums):
    new_nums = []
    for i_num in range(len(nums)):
        min_number = min(nums)
        new_nums.append(min_number)
        nums.remove(min_number)

    return new_nums


numbers = [random.randint(-10, 10) for i_number in range(10)]
print('Несортированный список: ', numbers)
sorted_nums = min_sort(numbers)
print('Сортированный список: ', sorted_nums)


