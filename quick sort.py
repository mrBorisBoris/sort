
def quick_sort(elements):
    if len(elements) <= 1:
        return elements
    element = elements[len(elements) // 2]
    left = list(filter(lambda x: x < element, elements))
    center = [x for x in elements if x == element]
    right = list(filter(lambda x: x > element, elements))

    return quick_sort(left) + center + quick_sort(right)


numbers = [9, 2, 4, 6, 2, 1, 3]
print(quick_sort(numbers))

