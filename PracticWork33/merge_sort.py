def merge_sort(lst: list) -> list:
    """
    Sorts a list of integers in non-descending order using the merge sort algorithm.

    Preconditions:
    - lst is a list (may be empty)
    - every element of lst is an integer or float

    Postconditions:
    - result is a list of the same length as lst: len(result) == len(lst)
    - result is sorted in non-descending order:
        for all i in range(len(result) - 1): result[i] <= result[i+1]
    - result is a permutation of lst (contains exactly the same elements):
        sorted(result) == sorted(lst)  [i.e. multiset equality]

    Invariants (merge step):
    - at every recursive call the sublists being merged are individually sorted
    - the merged output preserves all elements from both halves
    """
    if len(lst) <= 1:
        return list(lst)

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
