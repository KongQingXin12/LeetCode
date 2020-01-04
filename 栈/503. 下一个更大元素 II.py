from typing import List


# #  修修补补 通关
# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         if len(nums) == 0:
#             return nums
#         m = len(nums)
#         flag = [0] * m
#         Max = max(nums)
#         res = [0] * m
#         for j in range(m):
#             if nums[j] == Max:
#                 flag[j] = 1
#                 res[j] = -1
#         stack = []
#         i = 0
#         while i < m and flag[i] == 1:
#             i += 1
#         if i == m:
#             return [-1] * m
#         stack.append(i)
#         while stack:
#             while nums[i] > nums[stack[-1]]:
#                 res[stack[-1]] = nums[i]
#                 flag[stack[-1]] = 1
#                 stack.pop()
#                 if not stack: break
#             while nums[i] == Max:
#                 i = (i + 1) % m
#             if flag[i] == 0 and i not in stack:
#                 stack.append(i)
#             i = (i + 1) % m
#         return res


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        m = len(nums)
        res = [-1] * m
        stack = []

        for index, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                res[stack[-1]] = num
                stack.pop()
            stack.append(index)
        for num in nums:
            while stack and nums[stack[-1]] < num:
                res[stack[-1]] = num
                stack.pop()
            if not stack: break

        return res


if __name__ == '__main__':
    nums = [1, 2, 1, 2, 1, 2, 1, 21, 2, 12]
    S = Solution()
    print(S.nextGreaterElements(nums))
