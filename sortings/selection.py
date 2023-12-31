# Selection sort algorithm

# Selection sort is a comparison-based sorting algorithm. It splits the input list into two sections: a sorted portion and an unsorted portion. 
# The algorithm repeatedly identifies the minimum (or maximum) element in the unsorted section and moves it to the end (or beginning) of the sorted section. This process is iterated until the entire list is sorted.
# Selection sort maintains two subarrays within the input list: the left subarray, which contains sorted elements, and the right subarray, which holds unsorted elements. 
# During each iteration, the algorithm selects the minimum (or maximum) element in the unsorted subarray and swaps it with the leftmost element of the unsorted section. This operation effectively expands the sorted subarray.
# While selection sort is straightforward to implement, it has a time complexity of O(n^2) in the worst case, which makes it inefficient for sorting large datasets. 


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # if found an element less than the current element, swap these elements
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]


arr = [4, 8, 5, 1, 9, 6, 3, 7, 2, 10]
print("Original list:", arr)

selection_sort(arr)
print("Sorted list:", arr)