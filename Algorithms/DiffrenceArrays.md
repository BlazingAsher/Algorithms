<!-- TOC -->

- [Difference Arrays](#difference-arrays)

<!-- /TOC -->
# Difference Arrays
[prefix sums](https://github.com/YusufTaha/Algorithms/blob/master/Algorithms/PrefixSums.md) are used so that we don’t have to
repeatedly find the sums in an array. But how do we make that array? Lil’ Jami told us the exact index to update. But what if it gave
you a portion of the array that needs to be incremented by __X__? This doesn’t sound so bad when you only have an array of length 10. But
what if the array has a length over 1e+6, and we needed to increment every single item by __N__. Needless to say, this is rather inefficient.

Lets look at our array from Prefix sums again: `[a, a+b, a+b+c, a+b+c+d]`. The values of the items are all affected by the items previous to it. This is where
the Difference Array algorithm stems from. Instead of having an array of values and wanting to figure out the sums with minimal operations, we adjust an array
while knowing that the prefix sum algorithm will be applied to it at the end.

Here is an example. Lets say we had an array `A` with values `[0,0,0,0,0,0]`. Now we want to increment all items from the start to the end of the array by 1. The naive approach is looping through every item in array A and set its value to be += 1. But what if we have to do this 1e10 times, and the length of the array is 10^6?

If we want to increment array A by X from point P1 to P2 &nbsp;__0<= P1<P2 <= len(A)-1__&nbsp;, we can set __A[P1]__ to be += __X__, and &nbsp;__A[P2+1]__&nbsp; to be -= __X__. This causes us to only increment two items per change, rather than up to the length of A.
So to go from `[0,0,0,0,0,0]` to `[0,2,2,2,2,0]`, we would increment __A[1]__ by 2 and __A[5]__ by -2. This gets us `[0,2,0,0,0,-2]`.
