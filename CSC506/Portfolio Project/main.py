from collections import deque


def edmonds_karp(graph, source, sink):

    def bfs(residual_graph, source, sink, parent):
        # Initialize all vertices as not visited
        visited = set()
        queue = deque()

        # Add source to queue and mark it as visited
        queue.append(source)
        visited.add(source)

        # Standard BFS Loop
        while queue and sink not in visited:
            u = queue.popleft()
            for v in residual_graph[u]:
                # If vertex hasn't been visited and has capacity
                if v not in visited and residual_graph[u][v] > 0:
                    queue.append(v)
                    visited.add(v)
                    parent[v] = u

        # Return True if we reached sink in BFS
        return sink in visited

    # Initialize residual graph
    residual_graph = {u: graph[u].copy() for u in graph}
    for u in graph:
        for v in graph[u]:
            if u not in residual_graph[v]:
                residual_graph[v][u] = 0

    max_flow = 0
    parent = {}

    # Augment the flow while there is path from source to sink
    while bfs(residual_graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink

        # Find minimum residual capacity of the edges along the path
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        # Update residual capacities
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

        parent.clear()

    return max_flow


graph = {
    0: {1: 16, 2: 13},
    1: {2: 10, 3: 12},
    2: {1: 4, 4: 14},
    3: {2: 9, 5: 20},
    4: {3: 7, 5: 4, 6: 12},
    5: {},
    6: {4: 5}
}

source = 0
sink = 5

max_flow = edmonds_karp(graph, source, sink)
print(f"Maximum flow from vertex {source} to vertex {sink}: {max_flow}")
