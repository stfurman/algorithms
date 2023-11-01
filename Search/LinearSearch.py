# Linear search (aka sequential search)

# - is a method for finding an element within a list. It sequentially checks each element of the list until a match is found or the whole list has
# been searched. Linear search runs in at worst linear time and makes at most n comparisons, where n is the length of the list. If each element is
# equally likely to be searched, then linear search has an average case of n/2 comparisons, but the average case can be affected if the search
# probabilities for each element vary. Linear search is rarely practical because other search algorithms and schemes, such as the binary search
# algorithm and hash tables, allow significantly faster searching for all but short lists.


def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i

    return "Not found"

arr = [1,2,3,4,5,6,7,8,9,10]
key = int(input("Enter the key: "))
index = linear_search(arr, key)

print(index)