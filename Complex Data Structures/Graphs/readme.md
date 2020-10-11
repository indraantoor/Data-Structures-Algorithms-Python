# Graphs
Graphs are the perfect data structure for modeling networks.

They’re composed of _nodes_, or _vertices_, which hold data, and _edges_, which are a connection between two vertices. 

A single node is a **vertex**.

When _no path exists_ between two vertices, a graph is **disconnected**.

## Representation
We typically represent the vertex-edge relationship of a graph in two ways: 
1. Adjacency List 
2. Adjacency matrix.

### Adjacency List
In an adjacency list, each vertex contains a list of the vertices where an edge exists. 

To find an edge, one looks through the list for the desired vertex.

### Adjacency Matrix
An adjacency matrix is a table. 
Across the top, every vertex in the graph appears as a column. Down the side, every vertex appears again as a row. 

Edges can be bi-directional, so each vertex is listed twice.

## Code's Overview
The two classes, _Vertex_ and _Graph_ are capable of representing the typical variations in graphs that occur in many different algorithms.

**Vertex:**

Uses a dictionary as an adjacency list to store connected vertices.
Connected vertex names are keys and the edge weights are values.
Has methods to add edges and return a list of connected vertices.

**Graph:**

Can be initialized as a directed graph, where edges are set in one direction.
Stores every vertex inside a dictionary
Vertex data is the key and the vertex instance is the value.
Has methods to add vertices, edges between vertices, and determine if a path exists between two vertices.

## Keywords You Should Know

- **Vertex**: A node in a graph.
- **Edge**: A connection between two vertices.
- **Adjacent**: When an edge exists between vertices.
- **Path**: A sequence of one or more edges between vertices.
- **Disconnected**: Graph where at least two vertices have no path connecting them.
- **Weighted**: Graph where edges have an associated cost.
- **Directed**: Graph where travel between vertices can be restricted to a single direction.
- **Cycle**: A path which begins and ends at the same vertex.
- **Adjacency Matrix**: Graph representation where vertices are both the rows and the columns. Each cell represents a possible edge.
- **Adjacency List**: Graph representation where each vertex has a list of all the vertices it shares an edge with.