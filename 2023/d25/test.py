from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def get_connected_nodes(self):
        connected_nodes = defaultdict(list)

        for node in self.graph:
            visited = set()
            self._dfs(node, visited, connected_nodes)

        return dict(connected_nodes)

    def _dfs(self, current, visited, connected_nodes):
        visited.add(current)
        connected_nodes[current].extend(visited)

        for neighbor in self.graph[current]:
            if neighbor not in visited:
                self._dfs(neighbor, visited, connected_nodes)

# Example usage:
g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)

connected_nodes = g.get_connected_nodes()

for node, connected_list in connected_nodes.items():
    print(f"Nodes connected to {node}: {connected_list}")