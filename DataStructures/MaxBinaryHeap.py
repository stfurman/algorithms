# Binary Max Heap

# A max-heap is a specialized binary tree-based data structure where each parent node has a value greater than or equal to the values of its children. The maximum value is always at the root, making it suitable for efficiently finding and removing the maximum element from a collection.
# A min-heap is similar but with the opposite order: each parent node has a value less than or equal to the values of its children, and the minimum value is at the root. Min-heaps are useful for finding and removing the minimum element efficiently.
# Both max-heaps and min-heaps are commonly used as the underlying data structure for priority queues and heap sort algorithms due to their efficient nature in maintaining the largest or smallest elements at the top.

# Max heapify func
def max_heapify(arr, i):

    largest = i
    
    # Check left child
    if (i*2 + 1) < len(arr):
        if (arr[i*2 + 1] > arr[largest]):
            largest = i*2 + 1
    
    # Check right child
    if (i*2 + 2) < len(arr):
        if (arr[i*2 + 2] > arr[largest]):
            largest = i*2 + 2
    
    # Swap elements if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest)


# visualize heap
def visualize_binary_heap_text_with_connectors(arr, index=0, depth=0):
    if index < len(arr):
        spaces = " " * (depth * 4)
        print(spaces + "└─" + str(arr[index]))
        visualize_binary_heap_text_with_connectors(arr, 2 * index + 1, depth + 1)
        visualize_binary_heap_text_with_connectors(arr, 2 * index + 2, depth + 1)


# Example usage of max heapify on a list
arr = [4, 3, 5, 1, 2, 6, 8, 7, 9, 10]
n = len(arr)

# Build a max-heap from the given list
for i in range(n // 2 - 1, -1, -1):
   max_heapify(arr, i)


# The list 'arr' is now a max-heap
print("Max-Heap:", arr)
visualize_binary_heap_text_with_connectors(arr)