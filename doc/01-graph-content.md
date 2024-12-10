### Graph Basic

A graph is a pair of G=(V(G), E(G)). 
V(G) is a non-empty set, called **a vertex set**. Each element  in it is called a vertext or a node.
E(G) for the set of edges between nodes is called **an edge set.**

### Adjacent

In an undirected graph `G = V(V, E)`.  If there is an edge `(u,v)`, that we called u and v are adjacent.  
A vertex $v \in V.$ The neighborhood of is the set of all adjacent vertices. Denoted by $N(v)$

### Degree

With a vertex v, the number of associated edges is called the **degree** of the vertex. Denoted by `d(v)` 
Handshake theorem: $\sum_{v\in V}d(v) = 2 |E|$

### Path

Walk: A walk is a sequence of edges connecting a series of vertices, which can be finite or infinite in length.
This is a sequence of edges $e_1, e_2, ...,e_k$. And it exists a vertex sequence $v_0, v_1,...,v_k$
:grapes: **Trace**: For a path w, like $e_1, e_2, ...,e_k$ . it is a trace.
:purse: **Circuit**: For a trach w, like $v_0 = v_k$, then it is called w with a circuit.
:package: **Cycle**: For a ciruit w, like $v_o = v_k$ is the only pair of points that appere repeatedly in the point sequence. Then it   	        is a cycle.

### Subgraph

For a graph $G = (V, E)$. There is another graph $H = (V^n, E^n)$ . And $(V^n \in V, E^n \in E)$, then H is the subgraph of G.

### connectivity

**Undirected Graphs**
For an undirected graph G = (V, E), u and v are said to be connected if there exists a pathway such that $v_0 = u, v_k = v, for \space u, v \in V$ . By definition, any vertex is connected to itself and the two endpoints of any edge are connected.
An undirected graph G = (V, E) is said to be a connected graph if it satisfies that **any two of its vertices** are connected, a property of G called connectivity.

**Directed graphs**
For a directed graph G = (V, E), u is said to be reachable to v if there exists a pathway such that $v_0 = u, v_k = v$, for $u, v \in V$. By definition, any vertex is reachable to itself, and any edge is reachable to its end point. (Connectivity in an undirected graph can also be regarded as bi-directional reachability.)
A directed graph is said to be **strongly connected** if its nodes are mutually accessible.
A directed graph is said to be **weakly connected** if a connected graph can be obtained by replacing edges with undirected edges.
Similarly to connected components, there are weakly connected components (extremely weakly connected subgraphs) and strongly connected components (extremely strongly connected subgraphs).