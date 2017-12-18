# Graph Theory Intro

A graph data structure consists of a finite , *and possibly mutable*, set of ordered pairs, called edges or arcs, of certain entities called nodes or vertices. A graph is represented by a pair of two sets `G<V, E>`
where V is the set of vertices and E is the set of edges



+ ### A Vertex
    Represented as a little circle.
    + A `Degree` or `Valency` denoted 𝛿(v) is how many edges are connected to a node
    + Count loops as 2 edges in valency
    + `Isolated vertex` is a vertex with degree 0
    + `adjacent` vertices to a vertex are vertices that are directly connected to it

+ ### An Edge
    Represented as a line connecting nodes.
    + an edge (e) is `incedent` to vertex(a) and vertex(b) if i connects them
    + A `Loop` is an edge that points to the vertex itself
    + An edge can be parallel to another (multigraphs) edges that are parallel to another edge have a multiplicity of 2
    + Can have distances ( Weighted graphs)
    + Can have direction (directed graphs)

+ ### graph terminology
    + A `undirected` graph is a graph with edges represented as sets of 2 vertices (unordered) e = {a, b}. A `directed` graph is a graph with edges represented as ordered pairs (tuples) e' = (a,b).
    + A graph is connected if there is an x,y path for x, y ∈ V
    > in other words if every vertex is connected to every other vertex

    > if a graph is not connected we consider Kappa(G) which is the number of connected subgraphs
    + a graph's `diameter` is the largest number of vertices which must be traversed in order to travel from one vertex to another when paths which backtrack, detour, or loop are excluded from consideration.
    ### Figure 1
    ![](Images/img1.png)


    ### ways to implement a graph

    + Adjacency list : an array of size V with each element in the array pointing to a linked list. The array is indexed by a vertex (vertices from 0 to v-1) or a hash. where each index or key points to alinked list of adjacent verticies
    + Object Oriented: where vertex is an object and has the attribute neighbours which stores the linked list
    + Implicitly represented graphs: where the adjacency of a vertex is a function or vertex.neghbours() is a method (which takes less space if you aren't going to use all verticies)


        Ignoring the implicit representation you need at best Θ(V + E) space


+ ### Also
    + `Walk` is a sequence of vertices and edges
    > `closed walk` is a walk that starts at a vertex and returns to it
    > `trivial walk` is a walk that goes through no edges (one vertex)
    + `Trail` is a walk with no repeated edges
    > a closed trail is called a `circiut`
    + `Path` a walk with no repeated vertices
    > a closed path is a `cycle`. The first and the last vertex can be repeated

<!--TL;DR a graph is formed by vertices and edges connecting the vertices -->
