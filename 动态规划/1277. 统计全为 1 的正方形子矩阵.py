from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        res = [[0] * (n + 1) for _ in range(m + 1)]
        cnt = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if res[i + 1][j + 1] == 0:
                        res[i + 1][j + 1] = 1
                    if res[i][j] and res[i + 1][j] and res[i][j + 1]:
                        res[i + 1][j + 1] += min(res[i][j], res[i + 1][j], res[i][j + 1])
                cnt += res[i + 1][j + 1]
        return cnt


if __name__ == '__main__':
    matrix = [
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0]
    ]
    S = Solution()
    print(S.countSquares(matrix))
