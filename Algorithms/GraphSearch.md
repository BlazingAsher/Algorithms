**Table Of Conetents**
<!-- TOC -->

- [Graph Search](#graph-search)
    - [Breadth First Search](#breadth-first-search)
        - [figure 1](#figure-1)

<!-- /TOC -->

# Graph Search
Navigating through a graph is one of the very first uses for graphs. The way you implement graph traversal varries depending on what you want to achieve. Some applications include web
+ Web crawling
+ Pathfinding
+ Finding shortest paths
+ Maze generation
+ finding all vertices within one connected component;


![](images/gif1.gif)

## Breadth First Search
BFS is one of the most famous graph traversal algorithms because of how broad it can search. In other words, BFS explores the starting node's neighbours before going to the next level of nodes.
> BFS is shown in [Fig. 1](###figure-1)

### figure 1
![](images/gif2.gif)
<code>hello</code>
```python
# bfs traversal the graph
def bfs(start :int, Adj :dict):
    level  = {start: None}
    parent = {start: None}

    frontier = [start] # what we reached in previous level
    i = 1
    while frontier: # as long as there are still nodes
        next = [] # i
        for node in frontier:
            for v in Adj[node]:
                if v not in level:
                    # shortest path length (in edges) {vertex:edges to start node}
                    level[v] = i
                    parent[v] = node
                    next.append(v)
        frontier = next
        i += 1
```