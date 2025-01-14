'''
Bubble Sort Algorithm

You are given a list of integers. Write a Python function to sort the list in ascending order using the Bubble Sort algorithm. Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process is repeated until the list is sorted.

Parameters:

lst (List of integers): The list to be sorted.

Returns:

A list of integers sorted in ascending order.

Example:

Input: lst = [64, 34, 25, 12, 22, 11, 90]
Output: [11, 12, 22, 25, 34, 64, 90]
'''


def bubble_sort(lst):
    n = len(lst)
    
    for i in range(n):
        flag = 1  # flag to check if a swap occurred
        for j in range(0, n - i - 1):  # each pass checks one fewer element
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # swap
                flag = 0  # set flag to 0 if a swap occurred
                
        if flag == 1:  # if no swaps, the list is already sorted
            break
    
    return lst


print(bubble_sort([1,2,5,3,6,7,0]))








