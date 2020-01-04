from typing import List
import copy


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        m 右边界
        n 下边界
        :param grid:
        :return:
        '''
        n = len(grid)
        m = len(grid[0])

        flag = copy.deepcopy(grid)

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:  # 远点continue
                    continue
                elif i == 0:  # 第一行只能接受其左面的值
                    flag[i][j] += flag[i][j - 1]
                elif j == 0:  # 第一列 只能接受其上面的值
                    flag[i][j] += flag[i - 1][j]
                else:
                    flag[i][j] += min(flag[i - 1][j], flag[i][j - 1])

        return flag[n - 1][m - 1]


if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    S = Solution()
    print(S.minPathSum(grid))
