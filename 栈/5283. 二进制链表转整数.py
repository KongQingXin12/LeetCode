# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head != None:
            res = res << 1
            if head.val:
                res += 1
            head = head.next
        return res


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(0)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(0)
    S = Solution()
    S.getDecimalValue(head)
