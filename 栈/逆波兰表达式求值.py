from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        keys = ['+', '-', '*', '/']
        q = []
        m = len(tokens)
        for element in tokens:
            if element not in keys:
                q.append(element)
            else:
                b = int(q[-1])
                a = int(q[-2])
                q = q[:-2]
                if element == '+':
                    q.append(str(a + b))
                if element == '-':
                    q.append(str(a - b))
                if element == '*':
                    q.append(str(a * b))
                if element == '/':
                    q.append(str(abs(a) // abs(b) * 1 if a * b > 0 else abs(a) // abs(b) * -1))
        return int(q[0])


if __name__ == '__main__':
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    S = Solution()
    print(S.evalRPN(tokens))
