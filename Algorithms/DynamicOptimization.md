**Table Of Contents**
<!-- TOC -->

- [Dynamic Optimization](#dynamic-optimization)
    - [Sample problem](#sample-problem)
        - [The Greedy Solution](#the-greedy-solution)
        - [Pure Recursion](#pure-recursion)
        - [figure 1](#figure-1)
    - [Memoization](#memoization)

<!-- /TOC -->

# Dynamic Optimization
Recursion might be a "cool" way of doing iterative and not so iterative stuff, but sometimes recursion does some unnecessary computations.

## Sample problem

Let’s say I have three different denominations of coins:
+ 1 cent
+ 6 cents
+ 15 cents

Given a certain amount of money (in cents), what is the minimum number of coins needed?

### The Greedy Solution

Greedy algorithm works by choosing what looks like the best possible state at any given point, in the problem
Coin problem → choose the highest coin that can be taken out of the amount, repeat until amount is 0
Greedy algorithms work on many problems, but this is not one of them.

**Example**: greedy algorithm on 18 cents will yield

    15 + 1 + 1 + 1 → 4
Optimal solution is

     6 + 6 + 6 → 3
### Pure Recursion
+ The base case spoonful is zero
+ The current value can be broken down into one plus the minimum of the function called on the current value - 1, the current value - 6, and the current value - 15

```python
def mincents(number :int):
    if number == 0:
        return 0
    if number < 0:
        return 1e+9
    return 1 + min([mincents(number-1),mincents(number-6),mincents(number-15)])
```
**Cases**:
+ 1 : 1
+ 5 : 5
+ 6 : 1
+ 10: 5
+ 18: 3
+ 100: 10 `This one takes approximately 6 years of computation in pure recursion`

As you can see this is extremely inefficient as it has ,asymptotically, *O*(3ⁿ) time complexity. A lot of the computations are repeated, see [Fig.1](#figure-1)
### figure 1
## Memoization
Most of the computations are calculated more than once which is unnecessary. The solution is **memoizing** and as the name suggests the recursive algorithm is set up to realize overlapping solution subtrees.