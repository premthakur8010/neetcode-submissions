class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in match:  # closing bracket
                if not stack or stack[-1] != match[char]:
                    return False
                stack.pop()
            else:  # opening bracket
                stack.append(char)
        
        return len(stack) == 0