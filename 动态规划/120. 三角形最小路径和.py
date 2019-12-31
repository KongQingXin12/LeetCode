from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        if m == 1:
            return triangle[0][0]
        dp = [0] * (m + 1)
        for i in range(m - 1, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j + 1], dp[j]) + triangle[i][j]
        return dp[0]


if __name__ == '__main__':
    triangle = [
        [],
        # [3, 4],
        # [6, 5, 7],
        # [4, 1, 8, 3]
    ]
    S = Solution()
    print(S.minimumTotal(triangle))
