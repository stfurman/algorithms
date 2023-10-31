# Heap Sort

# Heap Sort is a comparison-based sorting algorithm. Heap sort can be thought of as an improved selection sort: like that algorithm, it 
# divides its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region by extracting the largest element
# and moving that to the sorted region. The improvement consists of the use of a heap data structure rather than a linear-time search to
# find the maximum.

def max_heapify(arr, N, i):

    largest = i
    
    left_child_index = i*2 + 1
    right_child_index = i*2 + 2

    if left_child_index < N and arr[left_child_index] > arr[largest]:
        largest = left_child_index
    
    if right_child_index < N and arr[right_child_index] > arr[largest]:
        largest = right_child_index
    
    # Swap elements if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, N, largest)


def heap_sort(arr):
    N = len(arr)
 
    # First, build a max-heap.
    for i in range(N//2 - 1, -1, -1):
        max_heapify(arr, N, i)

    # One by one extract elements and progressively reduce the heap
    for i in range(N-1, 0, -1):
        # Swap elements to put the largest element at the end of the *reduced* heap
        arr[i], arr[0] = arr[0], arr[i]  
        # Heapify the reduced heap 
        max_heapify(arr, i, 0)


# Example usage of delete_from_heap
arr = [4, 5, 3, 1, 2]
print("Unsorted list:", arr)

# Sort elements
heap_sort(arr)
print("Sorted list", arr)
