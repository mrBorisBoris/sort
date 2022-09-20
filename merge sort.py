def merge_lists(nums_a, nums_b):
    result = []
    i_index = j_index = 0
    while i_index < len(nums_a) and j_index < len(nums_b):
        if nums_a[i_index] < nums_b[j_index]:
            result.append(nums_a[i_index])
            i_index += 1
        else:
            result.append(nums_b[j_index])
            j_index += 1

    if i_index < len(nums_a):
        result += nums_a[i_index:]
    if j_index < len(nums_b):
        result += nums_b[j_index:]

    return result


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    middle = (len(numbers) // 2)
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])
    return merge_lists(left, right)


numbers = [1, 3, -1, 5, 2]
res = merge_sort(numbers)
print(*res)


