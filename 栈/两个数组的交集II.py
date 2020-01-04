from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)
        if m == 0 or n == 0:
            return []
        record = {}
        for i in nums1:
            if i in record:
                record[i] += 1
            else:
                record[i] = 1
        res = []
        for j in nums2:
            if j in record and record[j] > 0:
                res.append(j)
                record[j] -= 1
        return res
