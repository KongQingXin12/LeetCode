# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         stack = []
#         res = [0]
#         t=0
#         for i, ss in enumerate(s):
#             if ss == ')':
#                 if stack:
#                     stack.pop()
#                     if stack or res[-1] == 0:
#                         res.append(2)
#                     else:
#                         res[-1] += 2
#                 else:
#                     if res[-1]:
#                         res.append(0)
#             else:
#                 stack.append('(')
#         return max(res)

# !/usr/bin/env Python3.7
# coding=utf-8

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        res = []

        for i, ss in enumerate(s):
            if stack and ss == ')':
                res.append(stack.pop())
                res.append(i)
            elif ss == '(':
                stack.append(i)
        res.sort()
        Max_len = 0
        if not res: return 0
        stack = [res[0]]
        for j in range(1, len(res)):
            if res[j] == stack[-1] + 1:
                stack.append(res[j])
            else:
                Max_len = max(Max_len, len(stack))
                stack = [res[j]]
        Max_len = max(Max_len, len(stack))
        return Max_len


if __name__ == '__main__':
    s = "((()))())"
    S = Solution()
    print(S.longestValidParentheses(s))
