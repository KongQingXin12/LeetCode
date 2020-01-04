from typing import List


# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         res = []
#
#         def FindIndex(num: int) -> int:
#             pos = nums2.index(num)
#             for i in range(pos + 1, len(nums2)):
#                 if nums2[i] > num:
#                     return nums2[i]
#             return -1
#
#         for num in nums1:
#             res.append(FindIndex(num))
#
#         return res

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp = {}
        stack = []
        for i, num in enumerate(nums2):
            while stack and num > stack[-1]:
                temp[stack[-1]] = num
                stack = stack[:-1]
            stack.append(num)
        res = []
        for num1 in nums1:
            res.append(temp[num1] if num1 in temp else -1)
        return res


if __name__ == '__main__':
    S = Solution()
    nums1 = [3, 4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(S.nextGreaterElement(nums1, nums2))
