# Searching Algorithm's In Python

This is a repository made to help people who want to get started with data structures and algorithm's.

It is ideal for people who have just got started with learning about searching algorithm's.

This repository has the following search algorithm's in it:

1. Linear Search
2. Binary Search

## Linear Search

In computer science, search algorithms are step-by-step procedures used to locate and retrieve information from a set of data. This method in the example is similar to a search algorithm called linear search.

The linear search, or sequential search, algorithm sequentially checks whether a given value is an element of a specified list by scanning the elements of a list one-by-one. It checks every item in the list in order from the beginning to end until it finds a target value.

If it finds the target value in the list, the linear search algorithm stops and returns the position in the list corresponding to the target value. If it does not find the value, the linear search algorithm returns a message stating that the target value is not in the list.

### Find Elements In The List

Linear search can be used to search for a desired value in a list. It achieves this by examining each of the elements and comparing it with the search element starting with the first element to the last element in the list until it finds a match.

The steps are:

1. Examine the first element of the list.
2. If the first element is equal to the target value, stop.
3. If the first element is not equal to the target value, check the next element in the list.
4. Continue steps 1-3 until the element is found or the end of the list is reached.

### Best Case Performance

Linear search is not considered the most efficient search algorithm, especially for lists of large magnitudes. However, linear search is a great choice if you expect to find the target value at the beginning of the list, or if you have a small list.

The best case performance for linear search occurs when the target value exists in the list and is in the first position of the list. In this case, the linear search algorithm will only be required to make one comparison.

The time complexity for linear search in its best case is O(1).

### Worst Case Performance

There are two worst cases for linear search.

Case 1: when the target value at the end of the list.

Case 2: when the target value does not exist in the list.

In both cases, the linear search algorithm is required to scan the entire list of N elements and, therefore, makes N comparisons.

For this reason, the time complexity for linear search in its worst case is O(N).

### Time Complexity of Linear Search

Linear search runs in linear time. Its efficiency can be expressed as a linear function, with the number of comparisons to find a target increasing linearly as the size of the list, N, increases.

The time complexity for linear search in Big-O notation is O(N).

A time complexity of O(N) means the number of comparisons is proportional to the number of elements, N, in the list. With a list with twice as many elements, linear search will take at most twice as long to perform the search. The time complexity of linear search is also dependent on the best case, worst case, and average case scenarios.

Starting with linear search as a subroutine in your code is a useful foundation for constructing algorithms to solve more advanced search problems, such as:

Finding duplicates - sequentially search the list for all occurrences of the target value.

Finding the maximum value - sequentially scan the list for the largest value and track the largest value seen to date.

## Binary Search

With a sorted data-set, we can take advantage of the ordering to make a sort which is more efficient than going element by element.

Binary search requires a sorted data-set. We then take the following steps:

1. Check the middle value of the dataset.
2. If this value matches our target we can return the index.
3. If the middle value is less than our target
4. Start at step 1 using the right half of the list.
5. If the middle value is greater than our target
6. Start at step 1 using the left half of the list.

We eventually run out of values in the list, or find the target value.

### Time Complexity of Binary Search

How efficient is binary search?

In each iteration, we are cutting the list in half. The time complexity is O(log N).

A sorted list of 64 elements will take at most log2(64) = 6 comparisons.

In the worst case:

Comparison 1: We look at the middle of all 64 elements

Comparison 2: If the middle is not equal to our search value, we would look at 32 elements

Comparison 3: If the new middle is not equal to our search value, we would look at 16 elements

Comparison 4: If the new middle is not equal to our search value, we would look at 8 elements

Comparison 5: If the new middle is not equal to our search value, we would look at 4 elements

Comparison 6: If the new middle is not equal to our search value, we would look at 2 elements

When there’s 2 elements, the search value is either one or the other, and thus, there is at most 6 comparisons in a sorted list of size 64.

- By Indraan S. Toor
