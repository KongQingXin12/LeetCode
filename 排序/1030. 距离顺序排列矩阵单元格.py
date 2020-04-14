from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        def Sort(l: List[int], a: int, ans: List[List[int]], aa: List[int]):
            b = l[-1]
            if a <= l[0]:
                l.insert(0, a)
                ans.insert(0, aa)
            elif a >= l[-1]:
                l.append(a)
                ans.append(aa)
            else:
                for ll, i in enumerate(l):
                    if a >= ll:
                        l.insert(i + 1, a)
                        ans.insert(i + 1, aa)

        ans = []
        l = []

        for r in range(R):
            for c in range(C):
                a = abs(r - r0) + abs(c - c0)
                if len(l) == 0:
                    l.append(a)
                    ans.append([r, c])
                else:
                    Sort(l, a, ans, [r, c])

        return ans


if __name__ == '__main__':
    R = 2
    C = 2
    r0 = 0
    c0 = 1
    S = Solution()
    ans = S.allCellsDistOrder(R, C, r0, c0)
    print(ans)
