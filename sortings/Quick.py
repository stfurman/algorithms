# Quick sort

# Quick sort is a comparison-based sorting algorithm that uses divide-and-conquer to sort a list of elements.
# The algorithm divides the input list into two sublists by selecting a pivot element from the list and partitioning the other elements into two sublists, according to whether they are less than or greater than the pivot.
# The algorithm then recursively sorts the two sublists. The base case of the recursion is lists of size zero or one, which are always sorted.
# The pivot selection and partitioning steps can be done in several ways; the choice of specific implementation schemes greatly affects the algorithm's performance.
# The pivot selection determines the efficiency of the algorithm. If the pivot is chosen poorly, the algorithm can take quadratic time to sort the list.
# The partitioning step also affects the algorithm's performance. If the partitioning is balanced, the algorithm runs efficiently on a wide range of inputs.
# However, if the partitioning is unbalanced, the algorithm can take quadratic time to sort the list.
# The worst-case time complexity of quick sort is O(n^2), but it has an average time complexity of O(n log n).
# Quick sort is an unstable algorithm, which means that the relative order of equal elements is not preserved.
# The algorithm is also an in-place algorithm, which means that it does not require any extra space and can sort the list in situ.
# Quick sort is not a stable algorithm, which means that the relative order of equal elements is not preserved.
# The algorithm is also not an in-place algorithm, which means that it requires extra space to sort the list.
# The algorithm is also not adaptive, which means that it does not take advantage of existing order in the list.
# The algorithm is also not online, which means that it cannot sort a list as it receives it.
# The algorithm is also not a comparison sort, which means that it does not use comparisons to sort the list.
# The algorithm is also not a stable sort, which means that the relative order of equal elements is not preserved.


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose the pivot element (in this case, the middle element)
    
    left = []
    for x in arr:
        if x < pivot:
            left.append(x)

    middle = []
    for x in arr:
        if x == pivot:
            middle.append(x)

    right = []
    for x in arr:
        if x > pivot:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)



arr = [4, 8, 5, 1, 9, 6, 3, 7, 2, 10]
print("Original list:", arr)

sorted = quick_sort(arr)
print("Sorted list:", sorted)
