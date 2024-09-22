'''
Insertion Sort
Insertion Sort Algorithm

You are given a list of integers. Write a Python function to sort the list in ascending order using the Insertion Sort algorithm. Insertion Sort works by building a sorted section of the list, one element at a time, by inserting each new element into its proper position within the already sorted section.

Parameters:

lst (List of integers): The list to be sorted.

Returns:

A list of integers sorted in ascending order.

Example:

Input: lst = [12, 11, 13, 5, 6]
Output: [5, 6, 11, 12, 13]

Input: lst = [31, 41, 59, 26, 41, 58]
Output: [26, 31, 41, 41, 58, 59]'''


def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):  # Start from the second element
        current_ele = lst[i]  # The element to be inserted
        j = i - 1
        
        # Shift elements that are greater than current_ele
        while j >= 0 and lst[j] > current_ele:
            lst[j + 1] = lst[j]  # Shift the larger element to the right
            j -= 1
        
        # Place current_ele at its correct position
        lst[j + 1] = current_ele
    
    return lst




print(insertion_sort([31, 41, 59, 26, 41, 58]))



