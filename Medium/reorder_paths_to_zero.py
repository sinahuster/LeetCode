"""
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree).
Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

Constraints:
2 <= n <= 5 * 10^4
connections.length == n - 1
connections[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
"""

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        roads = set()
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            roads.add((a, b))
        
        def dfs(node):
            ans = 0
            for neighbor in graph[node]:
                if neighbor not in seen:
                    if (node, neighbor) in roads:
                        ans += 1
                    seen.add(neighbor)
                    ans += dfs(neighbor)
            return ans

        seen = {0}
        return dfs(0)

# this is a directed graph but we treat it as undirected 
# we use dfs to move away from 0, if we see this connection in connections 
# we know we need to swap it
# This has time and space complextity O(n)