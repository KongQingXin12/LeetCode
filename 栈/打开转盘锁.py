from collections import deque


class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends = set(deadends)
        if "0000" in deadends:  # 如果连起点都不能走就88
            return -1

        queue = deque()
        queue.append(["0000", 0])
        cnt = 0

        while queue:
            node, cnt = queue.popleft()  # 取一个点出来，cnt是当前走的步数
            if node == target:  # 找到了
                return cnt

            for i in range(4):
                for j in [1, -1]:
                    a = node[:i]
                    b = str((int(node[i]) + j) % 10)
                    c = node[i + 1:]
                    next_node = node[:i] + str((int(node[i]) + j) % 10) + node[i + 1:]

                    if next_node not in deadends:  # 新的点可以走而且没走过
                        deadends.add(next_node)  # 避免重复
                        queue.append([next_node, cnt + 1])

        return -1


# 解法2。速度很快，内存占用少（666）
from typing import List

# class Solution:
#     def openLock(self, deadends: List[str], target: str) -> int:
#         # 定义一个距离函数，计算target和'0000' 的距离
#         def dist(code):
#             return sum([min(int(c), 10 - int(c)) for c in code])
#
#         if "0000" in deadends or target in deadends:
#             return -1
#
#         new_codes = []
#         for i in range(4):
#             pre, x, sur = target[:i], int(target[i]), target[i + 1:]
#             new_codes.append(pre + str((x + 1) % 10) + sur)
#             new_codes.append(pre + str((x - 1) % 10) + sur)
#         # 计算target的上一步节点的集合（不在deadends中的）
#         moves = set(new_codes) - set(deadends)
#         if not moves:
#             return -1
#
#         result = dist(target)
#         for move in moves:
#             if dist(move) < result:
#                 return result
#         return dist(move) + 1  # 近的话，就是正常到target的距离；的话必须绕路再增加一步到target


if __name__ == '__main__':
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    S = Solution()
    print(S.openLock(deadends, target))
