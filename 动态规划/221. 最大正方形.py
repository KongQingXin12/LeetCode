from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        :param matrix: 
        :return:
        n:下边界
        m：右边界 
        '''
        n = len(matrix)
        if n == 0: return 0
        m = len(matrix[0])
        if m == 0: return 0
        if m == 1: return int(matrix[0][0])
        Max = 0
        flag = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i - 1][j - 1] == '1':
                    flag[i][j] += min(flag[i - 1][j], flag[i][j - 1], flag[i - 1][j - 1]) + 1
                    Max = max(flag[i][j], Max)
        return Max * Max


if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    S = Solution()
    print(S.maximalSquare(matrix))
