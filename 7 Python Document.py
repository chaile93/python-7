#!/usr/bin/env python
# coding: utf-8

# # Algorithms, Binary Search & Linked Lists

# ## Tasks Today:
#  
# 1) <b>In-Place Algorithms</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Syntax <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Out of Place Algorithm <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) In-Class Exercise #1 <br>
# 2) <b>Two Pointers</b> <br>
# 3) <b>Linked Lists</b> <br>
# 4) <b>Merge Sort</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Video on Algorithms <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) How it Works <br>
# 5) <b>Exercises</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Exercise #1 - Reverse a List in Place Using an In-Place Algorithm <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Exercise #2 - Find Distinct Words <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Exercise #3 - Write a program to implement a Linear Search Algorithm. <br>

# ## In-Place Algorithms

# #### Syntax

# In[ ]:


def swap(a_list, x, y, z):
    a_list[x], a_list[z], a_list[y], a_list[x]
    return a_list

my_list = [20, 4, 10]
print(f'Before swap: {my_list}')
print(my_list[0])
      
swap(my_list, 0, 1, 2)

print(f"After swap: {my_list}")
print(my_list[0])


# #### Out of Place Algorithm

# In[14]:


my_list_copy = my_list[:: -1]


array = ['e', 'b', 'c', 'd']
new_array = ['a'] * len(array)

print("Before ", array)
length = len(array)- 1

for i in range(length):
    new_array[1] = array[length - i]
    
array = new_array
print("After ", new_array)
print("Original", array)


# #### In-Class Exercise #1 <br>
# <p>Write a function that takes in four arguments (list, index1, index2, index3), and swaps those three positions in the list passed in.</p>

# In[15]:


def swap_positions(lst, index1, index2, index3):
    # Check if indices are within bounds of the list
    if 0 <= index1 < len(lst) and 0 <= index2 < len(lst) and 0 <= index3 < len(lst):
        # Swap the elements at the specified indices
        lst[index1], lst[index2], lst[index3] = lst[index3], lst[index1], lst[index2]
    else:
        # Handle invalid indices (if desired, raise an error or return None)
        print("Error: One or more indices are out of bounds")

# Example usage:
my_list = [10, 2, 3, 4, 5, 6, 8]
print("Original list:", my_list)

# Swap positions at indices 1, 2, and 4
swap_positions(my_list, 1, 2, 4)
print("Swapped list:", my_list)


# ## Two Pointers

# #### Syntax

# In[18]:


def twoPointers(alert):
    left = 0
    right = len(alist) - 1
    
    while left <= right:
        alist[left], alist[right] = alist[right], alist[left]
        left += 1
        right -= 1
    return alist
my_list2 = [1,2,3,12,9,8,4,11,22]
twoPointers(my_list2)


# #### Video of Algorithms <br>
# <p>Watch the video about algorithms.</p>
# 
# https://www.youtube.com/watch?v=Q9HjeFD62Uk
# 
# https://www.youtube.com/watch?v=kPRA0W1kECg
# 
# https://www.youtube.com/watch?v=ZZuD6iUe3Pc

# # Sorting Algorithms

# #### Bubble Sort
# 
# Worst Case: O(n^2) Time - O(1) Space

# In[ ]:


def swap(i, j, array):
    array[i], array[j], array[i]
    
def bubbleSort(array):
    isSorted = False
    while not isSorted:
        isSorted = True
        for num in range(len(array) - 1):
            if array[num] > array[num+1]:
                swap(num, num + 1, array)
                isSorted = False
    return array
bubbleSort([22, 55, 88, 44, 1, 100, 34, 66])


# ##### Insertion Sort
# 
# Worst Case: O(n^2) time - O(1)space

# In[ ]:


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    
def insertionSort(array)
    for i in range(1, len(array)):
        j = i


# ## Merge Sort

# #### How it Works

# In[ ]:


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Splitting the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sorting each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merging the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    left_index = right_index = 0
    
    # Merge the two halves into a sorted list
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1
    
    # Append remaining elements
    sorted_list.extend(left[l


# # Binary Search
# 
# The Binary Search algorithm works by finding the number in the middle of a given array and comparing it to the target. Given that the array is sorted
# 
# * The worst case run time for this algorithm is `O(log(n))`

# In[ ]:


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        
        if guess == target:
            return mid  # Found the target at index mid
        elif guess < target:
            low = mid + 1  # Target is in the right half
        else:
            high = mid - 1  # Target is in the left half
    
    return -1  # Target not found

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13
index = binary_search(arr, target)

if index != -1:
    print(f"Target {target} found at index {index}")
else:
    print(f"Target {target} not found in the array")


# # Exercises

# ### Exercise #1 <br>
# <p>Reverse the list below in-place using an in-place algorithm.<br>For extra credit: Reverse the strings at the same time.</p>

# In[ ]:


words = ['this' , 'is', 'a', 'sentence', '.']


# ### Exercise #2 <br>
# <p>Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.<br>Should output:<br>{'a': 5,<br>
#  'abstract': 1,<br>
#  'an': 3,<br>
#  'array': 2, ... etc...</p>

# In[23]:


a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

import re
from collections import defaultdict

def count_word_frequency(text):
    # Clean the text by removing punctuation and converting to lowercase
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Split the cleaned text into words
    words = cleaned_text.split()
    
    # Initialize a defaultdict to store word frequencies
    word_freq = defaultdict(int)
    
    # Count frequency of each word
    for word in words:
        word_freq[word] += 1
    
    return dict(word_freq)

# Example usage:
text = """
This is a sample text with words. Words are repeated to test the function. 
A function to count word frequencies and output a dictionary.
"""

result = count_word_frequency(text)
print(result)


# ## Exercise #3
# 
# Write a program to implement a Linear Search Algorithm. Also in a comment, write the Time Complexity of the following algorithm.
# 
# #### Hint: Linear Searching will require searching a list for a given number. 

# In[24]:


def linear_search(arr, target):
    """
    Perform linear search to find the target in the given array.
    
    Parameters:
    - arr (list): The list in which to search.
    - target: The value to search for in the list.
    
    Returns:
    - int: The index of the target if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage:
arr = [5, 8, 1, 3, 6, 9, 2]
target = 6
index = linear_search(arr, target)
if index != -1:
    print(f"Target {target} found at index {index}.")
else:
    print(f"Target {target} not found in the list.")

