class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree when there is no cycle
        # fully connected

        adj_map = {edge: [] for edge in range(n)}
        for a, b in edges:
            adj_map[a].append(b)
            adj_map[b].append(a)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in adj_map[node]:
                if (neighbor == parent):
                    continue

                if not dfs(neighbor, node):
                    return False

            return True
        
        if not dfs(0, -1):
            return False

        return len(visited) == n