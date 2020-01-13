from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 超时：递归
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         if len(lists) == 0: return None
#         if len(lists) == 1: return lists[0]
#
#         def merge2Lists(l1: ListNode, l2: ListNode) -> ListNode:
#             if l1 == None: return l2
#             if l2 == None: return l1
#             if l1.val < l2.val:
#                 l1.next = merge2Lists(l1.next, l2)
#                 return l1
#             else:
#                 l2.next = merge2Lists(l1, l2.next)
#                 return l2
#
#         res = lists[0]
#         for l in lists[1:]:
#             res = merge2Lists(res, l)
#         return res

# 超市：非递归
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         if len(lists) == 0: return None
#         if len(lists) == 1: return lists[0]
#
#         def merge2Lists(l1: ListNode, l2: ListNode) -> ListNode:
#             head = t = ListNode(0)
#             while l1 and l2:
#                 if l1.val < l2.val:
#                     t.next = ListNode(l1.val)
#                     l1 = l1.next
#                 else:
#                     t.next = ListNode(l2.val)
#                     l2 = l2.next
#                 t = t.next
#             if l1 != None:
#                 t.next = l1
#             if l2 != None:
#                 t.next = l2
#             return head.next
#
#         res = lists[0]
#         for l in lists[1:]:
#             res = merge2Lists(res, l)
#         return res

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = p = ListNode(0)

        node = []
        for l in lists:
            while l:
                node.append(l.val)
                l = l.next
        node.sort()
        for n in node:
            p.next = ListNode(n)
            p = p.next
        return head.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l3 = ListNode(2)
    l3.next = ListNode(6)

    lists = [
        l1, l2, l3
    ]
    S = Solution()
    ans = S.mergeKLists(lists)
    while ans:
        print(ans.val, end=' ')
        ans = ans.next
