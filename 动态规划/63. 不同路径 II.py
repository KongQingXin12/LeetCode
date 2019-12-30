from typing import List


# # 递归 超时
# class Solution:
#     cnt=0
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         n = len(obstacleGrid)  # 下边界
#         m = len(obstacleGrid[0])  # 右边界
#
#         if m==0 and n==1:return 1
#
#         def bfs(x: int, y: int):  # x 为横坐标，y 为纵坐标
#             if x == m or y == n or obstacleGrid[y][x] == 1:
#                 return
#             if x == m - 1 and y == n - 1:
#                 self.cnt += 1
#             bfs(x + 1, y)
#             bfs(x, y + 1)
#
#         bfs(0, 0)
#         return self.cnt


# 非递归


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        :param obstacleGrid:
        :return:
        n 下边界
        m 右边界
        '''
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        flag = [[0] * (m + 1) for _ in range(n + 1)]
        flag[1][1] = 1

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    flag[i + 1][j + 1] = 0
                else:
                    flag[i + 1][j + 1] += (flag[i][j + 1] + flag[i + 1][j])

        return flag[n][m]


if __name__ == '__main__':
    obstacleGrid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    S = Solution()
    print(S.uniquePathsWithObstacles(obstacleGrid))
