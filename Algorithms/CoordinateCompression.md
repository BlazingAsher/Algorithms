<!-- TOC -->

- [Coordinate Compression](#coordinate-compression)

<!-- /TOC -->
# Coordinate Compression
Prefix sums allow us to find the sums in an array with minimal calculation. Difference arrays allow me to increment values in an array with minimal adjusting. But what about the size of an array? Coordinate compression is used when the exact coordinates are not needed, or not fully needed, but what matters is relativity between points. This is useful when there are not that many test cases, but the test cases have very high numbers.
Here’s an example. Suppose I get a question that asks for the largest overlap in the grid, given rectangles. The way I would do this is figure out how many rectangles cover every point on the grid, and find out the largest number. But what’s interesting is that both of these inputs give the same result:
```
2 50 50			        2 5000 5000
20 20 40 50			2000 2000 4000
25 25 30 50			2500 2500 3000 3000
    ↓                                    ↓
    2                                    2
```
