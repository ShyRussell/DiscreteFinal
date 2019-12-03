### Shyheim Russell

# Discrete Final

## Dijkstra Shortest Path Algorithm

### What is Dijkstra Shortest Path Algorithm

 Dijkstra's Algorithm finds a shortest path tree from one single source node to other nodes using the minimum distances from the source.

 For these algorithms, the graphs has: vertices, or more commonly referred to as nodes, denoted by *v* or *u*. They also have weighted edges that connect two nodes (*u*, *v*) which denotes the edge and *w*(*u*, *v*) denotes the weight of each edge. Weight is equivalent to saying distance and how traversing that edge would affect the overall cost to travel.

 For this algorithm, you need to initialize three value:

* *dist* - An array of distances from the source node *s* to each node in the graph. You can do this through: *dist*(*s*) = 0 and all other nodes *v*, *dist*(*v*) = infinity.

  * This is done from the beginning because the algorithm would recalculate and finalize the *dist* when the shortest distance to *v* is found

* *Q* - a queue of all the nodes that exist in the graph, when the algorithm is done, *Q* will be empty.

* *S* - an empty set that indicates the nodes where the algorithm has visited and when the algorithm is done, *S* will contain all the nodes of the graph.


### Steps to the Algorithm

1. While *Q* is not empty, the algorithm with find the shortest path to node *v* from the source and pop node *v*, if not already in *S*  from *Q* with the smallest *dist*(*v*). In the first run, the source node will be chosen because the *dist*(*s*) = 0. The next node with the smallest distance from the source will then be chosen and popped from *Q* into *S*.

2. In order to indicate that a node has been visited, node *v* will be added to the set *S*.

3. The *dist* values will be updated fir the adjacent nodes of the current node *v* as follows: for each new adjacent node *u*.

  * if *dist*(*v*) + *weight(u, v)* < *dist(u)*, there is a new minimal distance found for *u*, so update *dist(u)* to the new minimal distance value

    * The weight of an edge *(u, v)* is taken from the value associated with *(u, v)* on the graph.

  * Otherwise, no updates are made to *dist(u)*

Once the algorithm has visited all the nodes in the graph and found the shortest distance for each node, *dist* now contains the shortest path tree from source *s*.

### Code Implementation Python Pseudo-Code

``` python
def Dijkstra(graph, s):
  dist[s] = 0                     # Initializing distance at source
  for v in range(graph):          # Initialization
    if v != source:
      dist[v] = float('inf')
    add v to Q

  while Q != 0:                     # The main loop
    v = Q[v] with min dist[v]       # First run-through, vertex is the source node
    remove v from Q

    for each neighbor u of v:       # Where the neighbor node u has not been removed from Q.
      alt = dist[v] + length(v, u)
      if alt < dist[u]:             # Finding a shorter path
        dist[u] = alt               # Update distance of u
  return dist[]
```

### Application


### Examples with Code
