#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @param head ListNode类
# @return bool布尔型


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        fast = head
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


if __name__ == "__main__":
    ln = ListNode(3)
    ln1 = ln.next = ListNode(2)
    ln2 = ln1.next = ListNode(0)
    ln3 = ln2.next = ListNode(-4)
    ln3.next = ln1
    s = Solution()
    res = s.hasCycle(ln)
    print(res)
