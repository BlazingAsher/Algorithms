<!-- TOC -->

- [Binary Search](#binary-search)
- [Implementation](#implementation)

<!-- /TOC -->
# Binary Search
Imagine having a pile of tests, and you want to get the one that is yours. You know that your mark was a 81%. If the pile was completely organized and unsorted, you would have to check every single test, which is a linear search. Worst case scenario, you need to check every single test.

But what if the pile was sorted according to something? By the names of the students, or by the marks on the test? Let's assume we know that the pile is sorted from lowest to highest grade. Would we really start from the very top until we find ours? We would take a test that lies around the half point, and see if that mark is above or below the mark we are looking for. We then take the pile the test could be in, and do the same, until we find our test. This reduces our search time significantly, and that is the idea of Binary Search. As a matter of fact, the worst case scenario would take __*O*(log N)__ (rounded up, base 2) attempts to find it. If there is a chance that none of the possibilities work, you would have to check the last possibility too, so you would have checked **log(N, base 2) + 1** different possibilities to see if they work, instead of N different possibilities.

With binary search, you need a sorted array You want to find the index of **X** with the minimal number of items to check. This requires us to have a portion of the list we want to check, the portion is where the **X** has a possibility of being. This portion is defined by lower and upper bounds. With the lower and upper bounds, we find the middle value by indexing the array at **(lowerBound+ upperBound)//2**, the average of the two indices.

The Lower bound is the lowest possible index of A where **X** may be found. If we search a mid point, and it is **<X**, then we know that **A[<= mid point]** will be **<X**. We then set the lower bound to the mid index + 1

The Upper bound on the other hand, is the highest possible index of A where **X** may be found. If we search a midpoint, and it is **>X**, then we know all values after that mid point will also be too large. Then, we set the Upper bound to the mid index -1

As we narrow the gap between the upper and lower bound, it is possible for the lower bound to exceed the upper bound, which would mean that **X** is not found.

# Implementation
```python
def binarySearch(array :int, X :int, lowerBound :int, upperBound :int):
while lowerBound <= upperBound:
		mid = (lowerBound + upperBound)//2
		if array[mid] == X:
			return mid
		if array[mid] < X:
			lowerBound = mid+1
		else:
			upperBound = mid-1
	return -1
```

Now, the idea of binary search is very intuitive, but implementing it in questions could be difficult. The hardest part is usually realizing it is a binary search question.
`It is a binary search question when you have a list,array,range of possibilities that can be sorted`, with a way to check if not only is a possibility correct or not, but if it is indexed before or after the answer.

**Example**: [Firehose](http://wcipeg.com/problem/ccc10s3)

The way we would do this question, is we consider every number from 0 to 100,000 a possibility. With the given hose distance, we would have to figure out if it’s possible or not, and change our upper and lower bounds accordingly.

To solve this question you would need two parts. The first is to figure out its a binary search question and structure it like so. The second is to figure out how to check if it is possible with the given distance, which is by figuring out the minimum number of hydrants needed with that distance and comparing it to the number of hydrants available.

```python

lowBound = 0
highBound = 1000000
while lowBound <= highBound:
    mid = (lowBound + highBound)//2 # The mid variable represents the hose length we are checking
    minHydrants = hydrantsNeeded(mid*2) # See how many hydrants we need for that hose reach

    if minHydrants <= numHydrants and mid == lowBound: # Lowest possible answer that works
        print(mid)
        break

    if minHydrants > num_hydrants: # Hose length is too short
        lowBound = mid+1
    else:                          # Hose length works, lets go smaller
        highBound = mid
```

Ending house is any house that could be at the end of reach, while 0 is the start.
it is false to assume that the best ending position is the last one that can reach from the start,
because perhaps there are ones from the other side that would have fit had the rope been able to extend more
``` python

def hydrantsNeeded(size :int): # Given a distance, we see the minimum number of hydrants needed
    hydrants = numHouses           # Worst case scenario, a hydrant is placed at each house
    endingHouse = 0

    while endingHouse < numHouses and houses[endingHouse] <= houses[0]+size:
        needed = 1                 # The number of hydrants we need, starts at 1 to connect the end house and the house at index 0
        end = houses[endingHouse]
        checkHouses = endingHouse+1

        while checkHouses < numHouses and houses[checkHouses] < houses[endingHouse]-size+1000000: # Make sure not to go out of index, and not to connect another hydrant if it reaches through the starting hose
            if houses[checkHouses] > end: # If it is out of reach, make a new hydrant
            end = houses[checkHouses] + size
            needed += 1

        checkHouses += 1

    hydrants = min(needed,hydrants) # set hydrants to the minimum possible value it could be
    endingHouse += 1

    return hydrants
```