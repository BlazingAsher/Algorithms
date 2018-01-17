<!-- TOC -->

- [Prefix Sums](#prefix-sums)
    - [figure 1](#figure-1)
    - [Implementation](#implementation)
- [Difference Arrays](#difference-arrays)
    - [Implementation](#implementation-1)

<!-- /TOC -->
# Prefix Sums
Given a question like [Lil jami](http://wcipeg.com/problem/liljami), you would repeatedly have to find the sum of a portion of your array.
You would find it fairly easy to complete the question. But to make runtime minimal, that is a different story. The general
idea is to have an array (or list) of length N, and update its values as the input is given. Then, repeatedly output the sum of the
items in the portion they ask for. That is rather inefficient though, as you will perform __*O*(N*K)__ operations, which could be up to
1e+12 (in Lil jami’s case).That is where the need of an algorithm comes in. The goal is to change your array, so that you will perform minimal operations once
asked to.
## figure 1
![](Images/img10.pngs)

 Given an array `[a, b, c, d]`, we can convert each item to be the sum of all the items before it and itself. This changes our array to `[a, a+b, a+b+c, a+b+c
 +d]`. With this new array, simply subtract to find the sum wanted.
> Example array in [Fig. 1](##figure-1)

**Example:** If we wanted to find the value of c+d
```python
# (a+b+c+d) - (a+b) = c+d
array[3] - array[1]
```
This leaves us with c+d in a single operation every time it is asked for.
## Implementation
+ __*Looping in the array and += each element to the item behind it*__
```python
# lets say the list is predefined somewhere in the code
for i in range(1,len(prefixList)):
    prefixList[i] += prefixList[i-1]
```

+ __*Making a new list, starting with 0 and adding from the last item*__
```python
newList = [0]
for item in prefixList:
    newList.append(item+newList[-1])
del newList[0]
```

# Difference Arrays
prefix sums are used so that we don’t have to
repeatedly find the sums in an array. But how do we make that array? Lil’ Jami told us the exact index to update. But what if it gave
you a portion of the array that needs to be incremented by **X**? This doesn’t sound so bad when you only have an array of length 10. But
what if the array has a length over 1e+6, and we needed to increment every single item by **N**. Needless to say, this is rather inefficient.

Lets look at our array from Prefix sums again: `[a, a+b, a+b+c, a+b+c+d]`. The values of the items are all affected by the items previous to it. This is where
the Difference Array algorithm stems from. Instead of having an array of values and wanting to figure out the sums with minimal operations, we adjust an array
while knowing that the prefix sum algorithm will be applied to it at the end.

Here is an example. Lets say we had an array `A` with values `[0,0,0,0,0,0]`. Now we want to increment all items from the start to the end of the array by 1. The naive approach is looping through every item in array A and set its value to be += 1. But what if we have to do this 1e10 times, and the length of the array is 10^6?

If we want to increment array A by X from point P1 to P2 &nbsp;**0<= P1<P2 <= len(A)-1**&nbsp;, we can set **A[P1]** to be += **X**, and &nbsp;**A[P2+1]**&nbsp; to be -= **X**. This causes us to only increment two items per change, rather than up to the length of A.
So to go from `[0,0,0,0,0,0]` to `[0,2,2,2,2,0]`, we would increment **A[1]** by 2 and **A[5]** by -2. This gets us `[0,2,0,0,0,-2]`.

For [Wireless](http://wcipeg.com/problem/ccc09s5), we need to count the number of bit rates attainable at every intersection. After that, we get the largest number and its count. Given these circles, how do we make our array of intersections?
## Implementation
First, we need a 2D Difference array __(next chapter)__, but we will be applying single array Difference arrays. The reason is because we are given the points to increment in the form of a circle, not a box.

```python
spots = [ [0 for a in range(lenY)] for b in range(lenX) ]
```
+ For every item given, loop through and get **x,y,r,s**
+ Loop through all y coordinates of the circle
+ Find both values of **x** in given **y**. Set the one with smaller index (or at index 0 if none exist) to += **s**, Set the larger index to += **s**.
+ Once done, apply the prefix sum algorithm to all arrays in spots.
+ Then find the largest number and its count
<!-- Need code -->
<!-- loop through all y values of circele get x from x = sqrt r**2 - y**2 -->
