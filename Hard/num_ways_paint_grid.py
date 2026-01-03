"""
You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: 
Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given n the number of rows of the grid, return the number of ways you can paint this grid. 
As the answer may grow large, the answer must be computed modulo 109 + 7.

Constraints:
n == grid.length
1 <= n <= 5000
"""

class Solution:
    def numOfWays(self, n: int) -> int:
        store = {}

        if n == 1:
            return 12

        def dfs(level, colours):
            if level == n:
                if colours == 2:
                    return 5
                else:
                    return 4

            if (level, colours) in store:
                return store[(level, colours)]
            
            if colours == 2:
                option_two = 3 * dfs(level + 1, 2)
            else:
                option_two = 2 * dfs(level + 1, 2)
            option_three = 2 * dfs(level + 1, 3)

            options = (option_two + option_three)
            store[(level, colours)] = options

            return options
        
        total = 2 * dfs(2, 2) + 2 * dfs(2, 3)
        return (3 * total) % (pow(10, 9) + 7)

        # 4 options for the first row assuming we start with red in the first cell
        # if we choose 2 colours: there are 5 options, 3 with 2 colours
        # if we choose 3 colours: there are 4 options, 2 with 2 colours    


# Time complexity is O(n), where n is the number of levels
# Space complexity is O(n), where n is the number of levels