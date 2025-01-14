'''
Selection Sort
Selection Sort Algorithm

You are given a list of integers. Write a Python function to sort the list in ascending order using the Selection Sort algorithm. Selection Sort works by repeatedly finding the minimum element from the unsorted part of the list and swapping it with the first element of the unsorted part.

Parameters:

lst (List of integers): The list to be sorted.

Returns:

A list of integers sorted in ascending order.

Example:

Input: lst = [64, 25, 12, 22, 11]
Output: [11, 12, 22, 25, 64]

Input: lst = [29, 10, 14, 37, 13]
Output: [10, 13, 14, 29, 37]
'''



def selection_sort(lst):
    n = len(lst)
    is_sorted = True  # Flag to check if the array is already sorted
    
    for i in range(n - 1):
        min_index = i  # Assume the current position is the minimum
        
        # Find the minimum element in the unsorted portion
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j  # Update min_index if a smaller element is found
        
        # Swap if a new minimum element was found
        if min_index != i:
            lst[min_index], lst[i] = lst[i], lst[min_index]
            is_sorted = False  # A swap occurred, so it's not sorted

    return lst




###
print(selection_sort([11, 25, 12, 22, 64]))
         
            


