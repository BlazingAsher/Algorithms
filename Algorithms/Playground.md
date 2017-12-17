#### Components
+ Placement of vertices and edges is irrelevant
+ Can be bidirectional
+ Edges can have a distance attribute

    ##### Vertices
    + The number of edges connected to a vertex is called a vertex's degree
    + Can have a degree of zero
    ##### Edges
    + Disconnected vs connected graphs
    + Components: couple of graphs in one
    Loops
    Directed edges
    parallel edges
    count loops twice in loops (by convention)
    + Are not mandatory between all vertices
    ##### Path & Length
        Sequence of distinct edges you
        can follow through a graph. The number
        of edges in this path is called its
        length

#### The Lingo
+ *Graph*  Collection of Vertices and Edges
+ *Vertex*  The little circles
+ *Edge*  The lines connecting the vertices
+ *Incident*  An edge between two vertices, e.g. an incident from A to B
+ *Adjacent*  pick a vertex V and all of the other vertices it connects to, V is adjacent to v_1, v_2, etc.
+ *Isolated*  A vertex that is all by itself, not connected to any other vertices
+ *Undirected/Directed*
+ *Walk*  a sequence of vertices and edges
+ *Closed Walk*  A walk where you end up at the same vertex that you started at
+ *Trail*  A walk with no repeated edges
+ *Circuit*  A closed trail
+ *Path*  A walk with no repeated vertices
+ *Cycle*  A closed path
+ *Connected Graph*  There is a path for all vertices to all other vertices
+ Denote the number of components with *k(G)*
+ *Simple Graph*  Loop free, no multiple edges