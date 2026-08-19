from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            currentWord, steps = queue.popleft()

            if currentWord == endWord:
                return steps

            for position in range(len(currentWord)):
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    newWord = currentWord[:position] + letter + currentWord[position + 1:]

                    if newWord in wordSet and newWord not in visited:
                        visited.add(newWord)
                        queue.append((newWord, steps + 1))

        return 0