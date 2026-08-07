class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []
        path = []

        def dfs(index):
            if index == len(digits):
                ans.append("".join(path))
                return

            for letter in phone[digits[index]]:
                path.append(letter)      # Choose
                dfs(index + 1)           # Explore
                path.pop()               # Undo

        dfs(0)
        return ans