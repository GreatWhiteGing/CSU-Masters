def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort the two halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both arrays and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


x = merge_sort([64, 34, 25, 12, 65, 22])
print(f"Sorted array: {x}")
