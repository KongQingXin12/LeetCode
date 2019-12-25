from numpy import stack


class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        for i, ss in enumerate(s):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                q.append(ss)
            else:
                if len(q) == 0: return False
                if ss == ')':
                    if q.pop() != '(':
                        return False
                if ss == ']':
                    if q.pop() != '[':
                        return False
                if ss == '}':
                    if q.pop() != '{':
                        return False
        if len(q): return False
        return True
