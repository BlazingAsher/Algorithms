<!-- TOC -->

- [Difference Arrays](#difference-arrays)
    - [Implementation](#implementation)

<!-- /TOC -->
# Difference Arrays
&nbsp;[prefix sums](https://github.com/YusufTaha/Algorithms/blob/master/Algorithms/PrefixSums.md) are used so that we don’t have to
repeatedly find the sums in an array. But how do we make that array? Lil’ Jami told us the exact index to update. But what if it gave
you a portion of the array that needs to be incremented by **X**? This doesn’t sound so bad when you only have an array of length 10. But
what if the array has a length over 1e+6, and we needed to increment every single item by **N**. Needless to say, this is rather inefficient.

&nbsp;Lets look at our array from Prefix sums again: `[a, a+b, a+b+c, a+b+c+d]`. The values of the items are all affected by the items previous to it. This is where
the Difference Array algorithm stems from. Instead of having an array of values and wanting to figure out the sums with minimal operations, we adjust an array
while knowing that the prefix sum algorithm will be applied to it at the end.

&nbsp;Here is an example. Lets say we had an array `A` with values `[0,0,0,0,0,0]`. Now we want to increment all items from the start to the end of the array by 1. The naive approach is looping through every item in array A and set its value to be += 1. But what if we have to do this 1e10 times, and the length of the array is 10^6?

&nbsp;If we want to increment array A by X from point P1 to P2 &nbsp;**0<= P1<P2 <= len(A)-1**&nbsp;, we can set **A[P1]** to be += **X**, and &nbsp;**A[P2+1]**&nbsp; to be -= **X**. This causes us to only increment two items per change, rather than up to the length of A.
So to go from `[0,0,0,0,0,0]` to `[0,2,2,2,2,0]`, we would increment **A[1]** by 2 and **A[5]** by -2. This gets us `[0,2,0,0,0,-2]`.

&nbsp;For [Wireless](http://wcipeg.com/problem/ccc09s5), we need to count the number of bit rates attainable at every intersection. After that, we get the largest number and its count. Given these circles, how do we make our array of intersections?
## Implementation
