# Bogo sort algorithm

# Bogo sort is a comparison-based sorting algorithm. It is a variation of the Fisher-Yates shuffle algorithm wherein the array is sorted and constantly checked if it is in the correct order.
# The algorithm repeatedly shuffles the array until the elements are in the correct order.
# Bogo sort is absolutely not a practical sorting algorithm and is primarily used for educational purposes on very small datasets.
# Bogo sort has an average time complexity of O(n * n!) and a worst-case time complexity of O(∞).

import random

def bogo_sort(list):
    while not is_sorted(list):
        shuffle(list)

def is_sorted(list):
    for i in range(0, len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True

def shuffle(list):
    for i in range(len(list)):
        r = random.randint(0, len(list) - 1)
        list[i], list[r] = list[r], list[i]


list = [4, 5, 8, 3, 2, 7, 6, 1, 10, 9] # reduce the number of elements if it take too long to sort :-P 
print("Original list:", list)
bogo_sort(list)
print("Sorted list:", list)