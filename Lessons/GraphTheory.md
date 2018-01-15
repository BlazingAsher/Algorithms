**Table Of Contents**
<!-- TOC -->

- [Graph Theory](#graph-theory)
    - [Figure 1](#figure-1)
    - [A node](#a-node)
    - [An Edge](#an-edge)
        - [Figure 2](#figure-2)
    - [graph terminology](#graph-terminology)
        - [Figure 3](#figure-3)
    - [ways to implement a graph](#ways-to-implement-a-graph)
        - [Figure 4](#figure-4)
    - [Trees](#trees)
    - [Connected components](#connected-components)
        - [Figure 5](#figure-5)

<!-- /TOC -->

# Graph Theory

A `graph` is a structure amounting to a set of objects in which some pairs of the objects are in some sense "related".

## Figure 1
![](Images/img1.png)

A graph is represented by a pair of two sets **G<V, E>** where **V** is the set of vertices and **E** is the set of edges

## A node
Represented as circles in [Fig. 1](#figure-1).
+ A `Degree` or `Valency` denoted 𝛿(v) is how many edges are connected to a node
+ `Isolated node` is a node with degree 0 (in [Fig. 1](#figure-1) node 10)
+ `adjacent vertices`  to a node are vertices that are directly connected to it.
>[Fig. 1](#figure-1) node **2** has an adjacent vertices **1** and **6**

## An Edge
Represented as a line connecting nodes in [Fig. 1](#figure-1).
+ an edge **e** is `incedent` to node **a** and node **b** if it connects them
+ A `Loop` is an edge that points to the node itself
>**Note** : Count loops as 2 edges in valency

> node 9 in [Fig. 1](#figure-1)
+ An edge can be parallel to other edges. We refer to the number of edges connecting to nodes directly with `multiplicity` of an edge. Graphs containing parallel edges are called `multi-graphs`
>[Fig. 1](#figure-1) edge connecting node **3** and node **8** has multiplicity of 2
+ `Weighted graphs` have distances on their edges
>[Fig. 1](#figure-1) edge connecting node **1** and node **3** has weight of 16 Kilometers
+ `directed graphs` have directed edges
>[Fig. 1](#figure-1) edge connecting node 3 and node 8)
+ `cycle` is a path of edges that go in a 'cycle' back to the starting node
+ a graph's `diameter` is the longest shortest path in a connected graph without backtracking or repeating edges or nodes
>refer to the yellow path in [Fig. 2](#figure-2).
### Figure 2
![](Images/img3.png)

## graph terminology
+ A `undirected` graph is a graph with edges represented as sets of 2 vertices (unordered) **e = {a, b}**. A `directed` graph is a graph with edges represented as ordered pairs (tuples/arrays) **e' = (a,b)**. Most graphs are either directed or undirected but a mix of both also exists

>[Fig. 1](#figure-1) is neither directed nor undirected graph
+ `Walk` is a sequence of vertices and edges
+ `Path` a walk with no repeated vertices
+ A graph is `connected` when there is a path between every pair of vertices
>[Fig. 3](#figure-3) is an example of a connected graph

>[Fig. 1](#figure-1) is an example of a disconnected graph.

### Figure 3
![](Images/img2.png)

<!--
> `closed walk` is a walk that starts at a node and returns to it
> `trivial walk` is a walk that goes through no edges (one node)
+ `Trail` is a walk with no repeated edges
>a closed trail is called a `circiut`
>a closed path is a `cycle`. The first and the last node can be repeated
-->


## ways to implement a graph

+ `Adjacency list` is an array of size **V** with each element in the array pointing to a linked list. The array is indexed by a node (vertices from 0 to v-1) or a hash. where each index or key points to a linked list of adjacent vertices

+ `Adjacency Matrix` is a matrix (traditionally a 2D array/list) where the element at an index represents the multiplicity of the edge between its indices

> [Fig. 4](#figure-4) represents a graph and it's Adjacency matrix

### Figure 4
![](Images/img4.png)

+ `OPP approach` is where node is an object and has the attribute neighbors which stores the linked list

+ `Implicit approach` is where the adjacency of a node is a function or **node.neighbors()** is a method (which takes less space if you aren't going to use all vertices)

**Ignoring the implicit representation you need a tight bound of Θ(V + E) space to store graph**

## Trees
+ A `tree` is an undirected graph in which any two vertices are connected by exactly one path.
> [Fig. 5](#figure-5) shows 3 trees and an isolated node
+ `Leaf nodes` are nodes without child nodes.
+ A `forest` is a disjoint collection of trees.

## Connected components
A `component` of an undirected graph is a subgraph that is completely disconnected than the other components
>[Fig. 5](#figure-5) shows a graph with 4 components

### Figure 5
![](Images/img6.png)
