# Understanding Dijkstra's Shortest Path Algorithm

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def new_node(self, value):
        self.nodes.add(value)

    def new_edges(self, start_node, end_node, distance):
        self.edges[start_node].append(end_node)
        self.edges[end_node].append(start_node)
        self.distance[(start_node, end_node)] = distnace

    def dijsktra(graph, initial):
        visited = {initial, 0}
        path = {}
        nodes = set(graph.nodes)

        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visted[min_node]

            for edge in graph.edges[min_node]:
                weight = current_weight + graph.distance[(min_node, edge)]
                if edge not in visited or weight < visited[edge]:
                    visted[edge] = weight
                    path[edge] = min_node

        return visited, path
