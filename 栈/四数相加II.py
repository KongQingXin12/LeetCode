from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        record = {}
        for a in A:
            for b in B:
                if a + b in record:
                    record[a + b] += 1
                else:
                    record[a + b] = 1
        res = 0
        for c in C:
            for d in D:
                temp = -(c + d)
                if temp in record:
                    res += record[temp]
        return res


if __name__ == '__main__':
    A = [-1, -1]
    B = [-1, 1]
    C = [-1, 1]
    D = [1, -1]
    S = Solution()
    print(S.fourSumCount(A, B, C, D))
