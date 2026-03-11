"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Constraints:
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        word_set = set(wordList)
        if endWord not in word_set:
            return 0 
        
        def valid_words(word):
            options = []
            for i in range(len(word)):
                for j in range(26):
                    ch = chr(97 + j)
                    if ch != word[i]:
                        new = word[:i] + ch + word[i + 1:]
                        if new in word_set:
                            options.append(new)
            return options 

        seen = {beginWord}
        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            
            for option in valid_words(word):
                if option not in seen:
                    seen.add(option)
                    queue.append((option, steps + 1))

        return 0
    

# this has time complexity O(n * L^2), where n is the word list length and L is the length of the word 
# and space complexity O(n)