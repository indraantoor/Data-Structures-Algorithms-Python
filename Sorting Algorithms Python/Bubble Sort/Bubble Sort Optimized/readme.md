# Bubble Sort (Optimized Working)
An implementation of the optimized version of Bubble Sort algorithm, written in Python.

You may have realized that we were doing some unnecessary iterations in unoptimized version.

## Working And Code Explanation
We know the last value in the list is in its correct position, so we never need to consider it again. 
The second time through the loop, we only need n-2 comparisons.

As we correctly place more values, fewer elements need to be compared. 

An optimized version doesn’t make n^2-n comparisons, it does (n-1) + (n-2) + ... + 2 + 1 comparisons, which can be simplified to (n^2-n) / 2 comparisons.

This is fewer than n^2-n comparisons but the algorithm still has a big O runtime of O(N^2).

As the input, N, grows larger, the division by two has less significance. 

Big O considers inputs as they reach infinity so the higher order term N^2 completely dominates.

We can’t make Bubble Sort better than O(N^2), but let’s take a look at the optimized code and compare iterations between implementations!

We will take advantage of parallel assignment in Python and abstracting away the **swap()** function.