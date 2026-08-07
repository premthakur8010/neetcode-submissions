class Solution:
    def partition(self, s: str):
        ans = []

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(start, path):
            # If we've partitioned the whole string
            if start == len(s):
                ans.append(path[:])
                return

            # Try every possible substring starting at 'start'
            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    path.append(s[start:end + 1])   # Choose
                    dfs(end + 1, path)              # Explore
                    path.pop()                      # Undo

        dfs(0, [])
        return ans