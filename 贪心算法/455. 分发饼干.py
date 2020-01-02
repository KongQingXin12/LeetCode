from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        '''
        :param g:
        :param s:
        :return: res
        '''
        g.sort()
        s.sort()
        res = 0
        for ss in s:
            if g and ss >= g[0]:
                res += 1
                g.pop(0)

        return res


if __name__ == '__main__':
    g = [1, 2]
    s = [1, 2, 3]
    S = Solution()
    print(S.findContentChildren(g, s))
