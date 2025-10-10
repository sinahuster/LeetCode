"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order

Contraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        answer = []

        for word in strs:
            ch = list(word)
            anagram = tuple(sorted(ch))
            if anagram not in count:
                count[anagram] = []
            count[anagram].append(word)

        for keys in count:
            answer.append(count[keys])

        return answer


"""
Turn the word into a list of characters, sort the list, turn it into a tuple, use this as key.
Add all words with the same tuple to the array of words, then add each array to the list result. 
This problem has time complexity O(n * k * log k) where n is the number of strings in strs, and k is the length of the longest string in strs. 
Then we have O(n) for iterating over each word in strs and O(k log k) for sorting each word in strs.
We have space complexity O(n * k) as this is the maximum size of the dictionary. 
"""