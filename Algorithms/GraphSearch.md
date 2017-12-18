# Graph Searching
Recape: A graph is a collection of nodes where each node might point to another nodes and the way they point might be directed or indirected.


#### Implementation of a graph
```python
```


The First problem a graph proves useful in is pathfinding or `Graph searching`. The problem is presented as follows: Im given node x can you go to node y?

There are ideally two ways to do this.
### Depth First search
This algorithm is recursive and priorotizes how deep the search gets rather than how wide.
### Breadth First search
This algorithm priorotizes how broadly the search is rather than how deep, and in BFS you need to use a qeue.


<!--
A graph in cpp
```cpp
#include "graphs.cc"

int main( int argc, char *argv[ ])
{
    Graph g;
    Search_Description s;
    vector<string> nodenames;

    nodenames.push_back("A");
    nodenames.push_back("B");
    nodenames.push_back("C");
    nodenames.push_back("D");
    nodenames.push_back("E");
    nodenames.push_back("F");

    for (int i = 0; i<6; i++)
    {
       for (int j = i+1; j<6; j++)
       {
          g.addEdge(nodenames[i],nodenames[j],i+j,"anon");
       }
    }

    g.shortestpaths("B");
    return 0;
}
```
-->