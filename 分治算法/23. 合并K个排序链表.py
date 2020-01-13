# %%

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge2Lists(l1: ListNode, l2: ListNode) -> ListNode:
            if l1 == None: return l2
            if l2 == None: return l1
            if l1.val < l2.val:
                return merge2Lists(l1.next, l2)
            else:
                return merge2Lists(l1, l2.next)

        res = ListNode(None)
        for l in lists:
            res = merge2Lists(res, l)
        return res


if __name__ == '__main__':
    lists = [

    ]
