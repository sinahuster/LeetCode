"""
You are assigned to put some amount of boxes onto one truck. 
You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. 
You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

Constraints:
1 <= boxTypes.length <= 1000
1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
1 <= truckSize <= 10^6
"""

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        ordered = sorted(boxTypes, key=lambda x:x[1], reverse=True)
        num = 0
        units = 0

        for i in range(len(ordered)):
            if ordered[i][0] + num <= truckSize:
                num += ordered[i][0] 
                units += ordered[i][0] * ordered[i][1]
            else:
                while num < truckSize:
                    num += 1 
                    units += ordered[i][1]

        return units            
    
# This has time conplexity O(n log n), where n is the length of boxTypes,
# and space complexity O(n)