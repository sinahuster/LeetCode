"""
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. 
Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x 
such that the edge colors alternate along the path, or -1 if such a path does not exist.

Constraints:
1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n
"""

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        RED = 0 
        BLUE = 1

        graph = defaultdict(lambda: defaultdict(list))
        for x, y in redEdges:
            graph[RED][x].append(y)
        for x, y in blueEdges:
            graph[BLUE][x].append(y)

        ans = [float("inf")] * n
        queue = deque([(0, RED, 0), (0, BLUE, 0)])
        seen = {(0, RED), (0, BLUE)}

        while queue:
            node, colour, steps = queue.popleft()
            ans[node] = min(ans[node], steps)

            for neighbour in graph[colour][node]:
                if (neighbour, 1 - colour) not in seen:
                    seen.add((neighbour, 1 - colour))
                    queue.append((neighbour, 1 - colour, steps + 1))
            
        return [x if x != float("inf") else -1 for x in ans]
    
# Time and space comeplexity is O(n + e) where e is the number of edges

