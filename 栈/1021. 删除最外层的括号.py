# https://leetcode-cn.com/problems/remove-outermost-parentheses/
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        res = []
        stack.append(0)
        for s in enumerate(S):
            if s[1] == ')':
                stack.pop()
                if len(stack) == 1:
                    res += S[stack[0] + 1: s[0]]
                    stack = [s[0] + 1]
            else:
                stack.append(s[0])
        return ''.join(res)


if __name__ == '__main__':
    S = Solution()
    Str = "(()())(())(()(()))"
    print(S.removeOuterParentheses(Str))
