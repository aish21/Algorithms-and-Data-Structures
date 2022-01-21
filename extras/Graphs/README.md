# Graphs
###### This section covers basic graphs concepts. 

- A graph is a non-linear data structure consisting of vertices and edges. 
- **Vertex** is a node in a graph
- **Path** - The sequence of vertices to go through from one vertex to another.
- **Path Length** - The number of edges in a path
- **Cycle** - A path where the starting point and endpoint are the same vertex.
- **Negative Weight Cycle** - In a weighted graph, if the sum of the weights of all edges of a cycle is a negative value.
- **Connectivity** - If there exists at least one path between two vertices, these two vertices are connected.
- **Degree of a Vertex** - The term degree applies to unweighted graphs. The degree of a vertex is the number of edges connecting the vertex.
- **In-Degree** - In-Degree is a concept in directed graphs. If the in-degree of a vertex is d, there are d directional edges incident to the vertex.
- **Out-Degree** - Out-Degree is a concept in directed graphs. If the out-degree of a vertex is d, there are d edges incident from the vertex.
- **Edge** - The connection between two vertices are the edges of the graph.
- **Undirected Graphs** - The edges between any two vertices in an undirected graph do not have a direction, indicating a two-way relationship.
- **Directed Graphs** - The edges between any two vertices in a directed graph are directional.
- **Weighted Graphs** - Each edge in a weighted graph has an associated weight, which can be of any metric.

## Disjoint Sets
- Also known as union-find data structure
- Primary objective of disjoint sets is to address the connectivity between the components of a network.
- **Parent Node** - The direct parent node of a vertex (adjacent to it)
- **Root Node** - A node without a parent node - it can be viewed as the parent node of itself. Sometimes referred to as the head node.
- Connections can be direct or indirect
- Use sets (unions) to connect vertices and compare root nodes to check for connectivity 
- The find function finds the root node of a given vertex, the union function unions two vertices and makes their root nodes the same.
- Implementation with *Quick Find*: in this case, the time complexity of the find function will be O(1). However, the union function will take more time with the time complexity of O(N).
> - When initializing a union-find constructor, we need to create an array of size N with the values equal to the corresponding array indices; this requires linear time.
> - Each call to find will require O(1) time since we are just accessing an element of the array at the given index.
> - Each call to union will require O(N) time because we need to traverse through the entire array and update the root vertices for all the vertices of the set that is going to be merged into another set.
> - The connected operation takes O(1) time since it involves the two find calls and the equality check operation.
- Implementation with *Quick Union*: compared with the Quick Find implementation, the time complexity of the union function is better. Meanwhile, the find function will take more time in this case.
> - The same as in the quick find implementation, when initializing a union-find constructor, we need to create an array of size N with the values equal to the corresponding array indices; this requires linear time.
> - For the find operation, in the worst-case scenario, we need to traverse every vertex to find the root for the input vertex. The maximum number of operations to get the root vertex would be no more than the tree's height, so it will take O(N) time.
> - The union operation consists of two find operations which (only in the worst-case) will take O(N) time, and two constant time operations, including the equality check and updating the array value at a given index. Therefore, the union operation also costs O(N) in the worst-case.
> - The connected operation also takes O(N) time in the worst-case since it involves two find calls.
- *Union by rank* - The word “rank” means ordering by specific criteria. Previously, for the union function, we always chose the root node of x and set it as the new root node for the other vertex. However, by choosing the parent node based on certain criteria (by rank), we can limit the maximum height of each vertex.
- Rank refers to the height of each vertex - effectively avoid the possibility of connecting all vertices into a straight line.
- 