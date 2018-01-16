def dfs(Adj :dict, start :object, visited = None):
    if visited is None: # verices we already traversed
        visited = set()
    visited.add(start)
    children = Adj[start] - visited # children of the starting vertex
    for next in children:
        dfs(Adj = Adj, start = next, visited = visited)
    return visited

dfs(Adj = {1:{2,3},2:{5,4,1},3:{1,6},4:{2},5:{2},6:{3,7},7:{6}}, start = 1)