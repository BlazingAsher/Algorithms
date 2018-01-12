<!-- TOC -->

- [Coordinate Compression](#coordinate-compression)
    - [Implementation](#implementation)

<!-- /TOC -->
# Coordinate Compression
Prefix sums allow us to find the sums in an array with minimal calculation. Difference arrays allow me to increment values in an array with minimal adjusting. But what about the size of an array? Coordinate compression is used when the exact coordinates are not needed, or not fully needed, but what matters is relativity between points. This is useful when there are not that many test cases, but the test cases have very high numbers.
Here’s an example. Suppose I get a question that asks for the largest overlap in the grid, given rectangles. The way I would do this is figure out how many rectangles cover every point on the grid, and find out the largest number. But what’s interesting is that both of these inputs give the same result:
```
2  50 50			2    5000 5000
20 20 40 50			2000 2000 4000
25 25 30 50			2500 2500 3000 3000
    ↓                                    ↓
    2                                    2
```

## Implementation
Coordinate compression takes all the X co-ordinates given and all the Y co-ordinates given (and any other amount of co-ordinates).We sort them out, and then reassign all of them to their index.  Let's take the first test case
```python
    listY = [20, 25, 30, 40]
    listx = [20, 25, 50]
```
So instead of having two rectangles at sides **(20, 20, 40, 50)** and **(25, 25, 30, 50)**; they become **(0,0,3,2)** and **(1,1,2,3)**. I can now solve for that very efficiently and get the same output. Keep in mind that sometimes we will need to refer back to our **listX** and **listY**, to find out the true value of our positions.
**Example**: [Tinted Glass](http://wcipeg.com/problem/ccc14s4)
```python
# input and variables
glassNum = int(input())
tintWanted = int(input())
listX = []
listY = []
rects = []
# Getting all the input in our lists
for a in range (glassNum):
    x1,y1,x2,y2,t = [int(e) for e in input().split()]
    listX += [x1,x2]
    listY += [y1,y2]
    rects.append([x1,y1,x2,y2,t])
# Compress the lists
listX = list(set(sorted(listX)))
listY = list(set(sorted(listY)))
for rect in rects:
    rect[0] = listX.index(rect[0])
    rect[1] = listY.index(rect[1])
    rect[2] = listX.index(rect[2])
    rect[3] = listY.index(rect[3])

# Use 2D DA to get the tint factors
positions = [[0 for a in range(len(listX))] for b in range(len(listY))]
```
