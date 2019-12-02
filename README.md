### Shyheim Russell

# DiscreteFinal

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
