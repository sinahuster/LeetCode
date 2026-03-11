"""
You are given a list of bombs. 
The range of a bomb is defined as the area where its effect can be felt. 
This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote 
the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. 
These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

Constraints:
1 <= bombs.length <= 100
bombs[i].length == 3
1 <= xi, yi, ri <= 10^5
"""

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        n = len(bombs)

        # Create the graph
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]

                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    graph[i].append(j)
            
        def bfs(i):
            queue = deque([i])
            visited = set([i])
            while queue:
                curr = queue.popleft()
                for neighbour in graph[curr]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
            return len(visited)

        ans = 0
        for i in range(n):
            ans = max(ans, bfs(i))
        
        return ans 
    

# This has time complexity O(n^3) and space complexity O(n^2)