# Bubble Sort 
An implementation of the Bubble Sort algorithm written in Python.
## Bubble Sort: Swap Function
The Bubble Sort algorithm works by comparing a pair of neighbor elements and shifting the larger of the two to the right. 

Bubble Sort completes this by swapping the two elements’ positions if the first element being compared is larger than 
the second element being compared.

Bubble sort swaps elements repeatedly until the largest element in the list is placed at the greatest index. 
This looping continues until the list is sorted.

## Bubble Sort: Compare Function
We’ll have two loops:

One loop will iterate through each element in the list.

Within the first loop, we’ll have another loop for each element in the list.

Inside the second loop, we’ll take the index of the loop and compare the element at that index with the element 
at the next index. 

If they’re out of order, we’ll make a swap.

