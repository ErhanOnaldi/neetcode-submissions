class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        size = [1] * (len(edges) + 1)

        def find(x):
            root = x

            while parent[root] != root:
                root = parent[root]

            return root

        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return 0
            if size[root_b] > size[root_a]:
                parent[root_a] = root_b
                size[root_b] += size[root_a]
            else:
                parent[root_b] = root_a
                size[root_a] += size[root_b]

            return 1

        for a, b in edges:
            if union(a, b) == 0:
                return [a, b]



