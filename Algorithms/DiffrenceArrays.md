<!-- TOC -->

- [Difference Arrays](#difference-arrays)

<!-- /TOC -->
# Difference Arrays
[prefix sums](https://github.com/YusufTaha/Algorithms/blob/master/Algorithms/PrefixSums.md) are used so that we don’t have to
repeatedly find the sums in an array. But how do we make that array? Lil’ Jami told us the exact index to update. But what if it gave
you a portion of the array that needs to be incremented by X? This doesn’t sound so bad when you only have an array of length 10. But
what if the array has a length over 1e+6, and we needed to increment every single item by N. This is rather inefficient.

