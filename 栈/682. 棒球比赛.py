from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for num in ops:
            if num == '+':
                stack.append(stack[-1] + stack[-2])
            elif num == 'C':
                stack.pop()
            elif num == 'D':
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(num))
        res = 0
        for i in stack:
            res += i
        return res


if __name__ == '__main__':
    S = Solution()
    ops = ["5", "2", "C", "D", "+"]
    print(S.calPoints(ops))
