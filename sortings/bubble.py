# Bubble sort algorithm

# Bubble sort is a simple comparison-based sorting algorithm. 
# It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. 
# The pass through the list is repeated until the list is sorted.
# The key idea behind bubble sort is to repeatedly compare adjacent elements and swap them if they are out of order, effectively "bubbling" the largest (or smallest) element to the end (or beginning) of the list. This process is repeated for each element in the list until no more swaps are needed.
# Bubble sort has a worst-case time complexity of O(n^2), making it inefficient for sorting large lists, and it is primarily used for educational purposes or on small datasets. There are more efficient sorting algorithms available for practical use, such as quick sort, merge sort, and heap sort.


# Bubble sort using for loops
def bubble_sort_with_for_loops(list):
    for i in range(len(list) - 1, 0, -1):
        for j in range(0, i, 1):
            if (list[j] > list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]

list1 = [50, 20, 10, 30, 40, 66, 33, 77, 23, 5, 1, 3, 8]
print("Original list:", list1)

bubble_sort_with_for_loops(list1)
print("Sorted list:", list1)


print(" --- ")

# bubble sort with while loops
def bubble_sort(list):
    i = len(list) - 1
    while i > 0:
        j = 0
        while j < i:
            if (list[j] > list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]
            j += 1
        i -= 1
             

list2 = [22, 4, 55, 12, 57, 7, 49, 45, 2, 1, 3, 8]
print("Original list:", list2)

bubble_sort(list2)
print("Sorted list:", list2)
