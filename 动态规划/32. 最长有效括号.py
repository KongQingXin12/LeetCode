class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        res = [0]
        for i, ss in enumerate(s):
            if ss == ')':
                if stack:
                    if res[-1] == 0:
                        res.append(2)
                    else:
                        res[-1] += 2
                    stack.pop()
                else:
                    res.append(0)
            else:
                stack.append('(')
        return max(res)


if __name__ == '__main__':
    s = "(())()()()()()"
    S = Solution()
    print(S.longestValidParentheses(s))
