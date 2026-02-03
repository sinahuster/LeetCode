"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

Constraints:
1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def answer_query(start, end):
            if start not in graph:
                return -1

            seen = {start}
            stack = [(start, 1)]

            while stack:
                node, ratio = stack.pop()
                if node == end:
                    return ratio

                for neighbour in graph[node]:
                    if neighbour not in seen:
                        seen.add(neighbour)
                        stack.append((neighbour, ratio * graph[node][neighbour]))
                        
            return -1
        
        graph = defaultdict(dict)
        for i in range(len(equations)):
            numerator, denominator = equations[i]
            val = values[i]
            graph[numerator][denominator] = val
            graph[denominator][numerator] = 1/ val

        ans = [] 
        for numerator, denominator in queries:
            ans.append(answer_query(numerator, denominator))

        return ans 
    
    # This has time complexity O(q * (n + e)) where q is the length of queries, n is the number of variables and e is the number of equations 
    # and a space complexity of O(e)