class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        res = 0
        t = 0
        for Str in s:
            while stack and Str == ')':
                t += 2
                stack.pop()
