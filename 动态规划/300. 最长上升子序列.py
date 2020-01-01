from typing import List


# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if len(nums) <= 1: return len(nums)
#         stack = []
#         res = 0
#         for num in nums:
#             while stack and stack[-1] >= num:
#                 stack.pop()
#             stack.append(num)
#             res = max(res, len(stack))
#         return res


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return n
        res = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if nums[j] > nums[i]:
                    if res[i] >= (max(res[j:]) + 1):
                        break
                    res[i] = max(res[j] + 1, res[i])
        return max(res)


if __name__ == '__main__':
    nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]  # [10, 9, 2, 5, 3, 7, 101, 18]
    S = Solution()
    print(S.lengthOfLIS(nums))
