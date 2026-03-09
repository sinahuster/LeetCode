"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. 
If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

Constraints:
0 <= bank.length <= 10
startGene.length == endGene.length == bank[i].length == 8
startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
"""

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0

        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        def valid_mutations(gene):
            options = []
            for i in range(len(gene)):
                for ch in 'AGCT':
                    if ch != gene[i]:
                        new = gene[:i] + ch + gene[i + 1:]
                        if new in bank_set:
                            options.append(new)

            return options 

        seen = {startGene}
        queue = deque([(startGene, 0)])

        while queue:
            mutation, steps = queue.popleft()
            if mutation == endGene:
                return steps

            for option in valid_mutations(mutation):
                if option not in seen:
                    seen.add(option)
                    queue.append((option, steps + 1))
            
        return -1

# this has time and space complexity O(1)
# as the length of the genes is always 8 and the bank is also only up to 10 