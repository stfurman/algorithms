# Binary Heap

# A max-heap is a specialized binary tree-based data structure where each parent node has a value greater than or equal to the values of its children. The maximum value is always at the root, making it suitable for efficiently finding and removing the maximum element from a collection.
# A min-heap is similar but with the opposite order: each parent node has a value less than or equal to the values of its children, and the minimum value is at the root. Min-heaps are useful for finding and removing the minimum element efficiently.
# Both max-heaps and min-heaps are commonly used as the underlying data structure for priority queues and heap sort algorithms due to their efficient nature in maintaining the largest or smallest elements at the top.

# Max heapify func
def max_heapify(arr, i):
    
    left_child_index = 2 * i + 1
    right_child_index = 2 * i + 2
    
    largest = i
    
    # Check left child
    if left_child_index < len(arr):
        if (arr[left_child_index] > arr[largest]):
            largest = left_child_index
    
    # Check right child
    if right_child_index < len(arr):
        if (arr[right_child_index] > arr[largest]):
            largest = right_child_index
    
    # Swap elements if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest)


def _heapify_up(arr, index):
    while index > 0:
        parent_index = (index - 1) // 2
        print("Parent index=" + str(parent_index))
        if arr[index] > arr[parent_index]:
            arr[index], arr[parent_index] = arr[parent_index], arr[index]
            index = parent_index
        else:
            break

def _heapify_down(arr, index):
    while True: 
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if left_child_index < len(arr):
            if (arr[left_child_index] > arr[largest]):
                largest = left_child_index
        
        if right_child_index < len(arr):
            if (arr[right_child_index] > arr[largest]):
                largest = right_child_index

        if largest != index:
            arr[index], arr[largest] = arr[largest], arr[index]
            _heapify_down(arr, largest)
        else:
            break
   

# Insert element into heap
def insert_into_heap(arr, element):
    # Insert the new element at the end
    arr.append(element)
    n = len(arr)
    _heapify_up(arr, n-1)


# Delete element from from heap
def delete_from_heap(arr, value):
    if value in arr:
        index = arr.index(value)
        
        # Swap the element to be deleted with the last element
        arr[index], arr[-1] = arr[-1], arr[index]
        # Delete the last element
        arr.pop()
        # Heapify the root element
        n = len(arr)
        _heapify_down(arr, index)
    else:
        print("Could not find " + str(value) + " in heap")


# visualize heap
def visualize_binary_heap_text_with_connectors(arr, index=0, depth=0):
    if index < len(arr):
        spaces = " " * (depth * 4)
        print(spaces + "└─" + str(arr[index]))
        visualize_binary_heap_text_with_connectors(arr, 2 * index + 1, depth + 1)
        visualize_binary_heap_text_with_connectors(arr, 2 * index + 2, depth + 1)


# Example usage of max heapify on a list

# Read comma-separated values from the command line
input_str = input("Enter comma-separated values: ")

# Split the input string into an array
input_list = input_str.split(',')

# Convert the list of strings to a list of integers (if integers are expected)
arr = [int(item) for item in input_list]

print("Original list:", arr)
n = len(arr)
print("Total elements in list: " + str(n))

# Build a max-heap from the given list
for i in range(n // 2 - 1, -1, -1):
   max_heapify(arr, i)

# The list 'arr' is now a max-heap
print("Max-Heap:", arr)
visualize_binary_heap_text_with_connectors(arr)


# Insert an element in the heap
elementToInsert = input("Enter the element you want to insert into the heap: ")
insert_into_heap(arr, int(elementToInsert))
print("Modified max heap: ", arr)
visualize_binary_heap_text_with_connectors(arr)


# Delete an element from the heap
elementToDelete = input("Enter the element you want to delete from the heap: ")
delete_from_heap(arr, int(elementToDelete))
print("Modified max heap: ", arr)
visualize_binary_heap_text_with_connectors(arr)
