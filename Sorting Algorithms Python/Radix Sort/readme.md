# Radix Sort
Let's now understand and get to know what radix sort is 
and how it works.

## What Is Radix Sort?
Our number system was developed by 8th century Arabic mathematicians and was successful because it made arithmetic 
operations more sensible and larger numbers easier to write and comprehend.

The breakthrough those mathematicians made required defining a set of rules for how to depict every number. 

First we 
decide on an alphabet: different glyphs, or digits, that we’ll use to write our numbers with. The alphabet that we use 
to depict numbers in this system are the ten digits 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. 

We call the length of this alphabet our radix (or base). So for our decimal system, we have a radix of 10.

Next we need to understand what those digits mean in different positions. In our system we have a ones place, a tens 
place, a hundreds place and so on. 

There’s a difference, for instance, between the digit ‘4’ and the "number" four that we represent with the digit ‘4’. 

We use these digits to represent different values when they’re used in different 
positions. The digit 4 in the number 14 represents the value 4, but the digit 4 used in the number 27422 represents 
the value 400.

## Base Numbering Systems
The value of different positions in a number increases by a _multiplier of 10_ in increasing positions. 

This means that a digit ‘4’ in the rightmost place of a number is equal to the value 4, but that same digit when shifted left one position is equal to 10 * 4. 

If you shift it again one position you get 400, which is 10 * 10 * 4.

Since we have 10 digits (0-9), this system that we used is called **base-10** because of that.

## How Does It Work?
There are two different kinds of radix sort: 
1. **MSD**: Most Significant Digit 
2. **LSD**: Least Significant Digit

Both radix sorts organize the input list into ten _“buckets”_, one for each digit. 
The numbers are placed into the buckets based on the MSD (left-most digit) or LSD (right-most digit). 

**Example**: Number _3421_ would be placed into the bucket _“3” for MSD_ and into _“1” for LSD_.

This bucketing process is repeated over and over again until all digits in the longest number have been considered. 

The order within buckets for each iteration is preserved. 

## Performance
Radix sort manages to sort a list of integers without performing any comparisons and we can also call it a 
_non-comparision sort_.

Consider a list of length n. For each iteration of the algorithm, we are deciding which bucket to place each of the n entries into.

This means we need to iterate for how ever many digits we have. Let's call this average number of digits the _word-size_ or _w_.

This means the complexity of radix sort is **O(wn)**. 

Assuming the length of the list is much larger than the number of digits, we can consider w a constant factor and this can be _reduced_ to **O(n)**.