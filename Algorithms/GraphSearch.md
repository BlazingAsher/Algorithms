**Table Of Conetents**
<!-- TOC -->

- [Graph Search](#graph-search)
    - [Breadth First Search](#breadth-first-search)
        - [figure 1](#figure-1)
        - [Python BFS](#python-bfs)
            - [figure 2](#figure-2)
    - [Depth First Search](#depth-first-search)
        - [figure 3](#figure-3)

<!-- /TOC -->

# Graph Search
Navigating through a graph is one of the very first uses for graphs. The way you implement graph traversal varries depending on what you want to achieve. Some applications include:
+ Web crawling
+ Pathfinding
+ Finding shortest paths
+ Maze generation
+ finding all vertices within one connected component

**BFS pathfinding algorithm**

![](Images/gif1.gif)
## Breadth First Search
BFS is one of the most famous graph traversal algorithms because of how broad it can search. In other words, BFS explores the starting node's neighbours before going to the next level of nodes.
> BFS is shown in [Fig. 1](###figure-1)

### figure 1
**BFS in action**

![](Images/gif2.gif)

### Python BFS
```python
def bfs(start :int, Adj :dict):
    level  = {start: None} # {node: distance to starting node (# edges)}
    parent = {start: None} # the parent hash is optional but helps
                           # backtrack for shortest paths

    previous = [start] # what nodes in previous
                       # level (resets with each while iteration)
    i = 1
    while previous:
        next = []
        for node in previous:
            for neighbours in Adj[node]: # for children of previous nodes
                if neighbours not in level: # if it hasn't already been traversed

                    level[neighbours] = i
                    parent[neighbours] = node
                    next.append(neighbours)

        previous = next
        i += 1
# the graph is represented in Fig 2
bfs(start = 1, Adj = {1:{2,3},2:{5,4,1},3:{1,6},4:{2},5:{2},6:{3,7},7:{6}})
```



#### figure 2
![](Images/img5.png)

## Depth First Search
DFS is much more intuitive than BFS in traversal although it is the recursive approach. DFS traverses into a child of a starting node then goes to it's child and so on until there is no more cildren then it backtracks.

### figure 3
**DFS in action**
![](Images/gif3.gif)
```python
def dfs(start :int, Adj :dict):
    parent = {start: None}
    def search(start :int, Adj :dict):
        for neighbour in Adj[start]:
            if neighbour not in parent:
                parent[neighbour] = start
                search(start = neighbour, Adj = Adj)
    search(start, Adj)

dfs(start = 6, Adj = {1:{2,3},2:{5,4,1},3:{1,6},4:{2},5:{2},6:{3,7},7:{6}})
```