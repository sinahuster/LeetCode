"""
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.

Constraints:
1 <= matches.length <= 10^5
matches[i].length == 2
1 <= winneri, loseri <= 10^5
winneri != loseri
All matches[i] are unique.
"""

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        scores = {}
        answer = [[], []]

        for match in matches:
            winner = match[0]
            loser = match[1]

            if winner in scores:
                scores[winner][0] += 1
            else:
                scores[winner] = [1, 0]

            if loser in scores:
                scores[loser][1] += 1
            else:
                scores[loser] = [0, 1]
        
        for player in scores:
            if scores[player][1] == 0:
                answer[0].append(player)
            if scores[player][1] == 1:
                answer[1].append(player)

        answer[0].sort()
        answer[1].sort()
        return answer


# create a hash table of arrays with two values [wins, losses]
# when we encounter a player, check if they are in the hash table, if not add them
# increment the counter of wins or losses 
# check which players have [x, 0] and add to answer[0] and [x, 1] and add to answer[1]

# This soltuion has time complexity O(n log n) and space complexity O(n)